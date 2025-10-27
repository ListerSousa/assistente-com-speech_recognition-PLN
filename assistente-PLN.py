import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import wikipedia
import webbrowser
import pyjokes

# ----------------------------------------------------
# 1. MÓDULO TEXT-TO-SPEECH (TTS)
# ----------------------------------------------------
def falar(texto):
    """
    Função que transforma texto em áudio e o reproduz.
    """
    print(f"Assistente: {texto}")
    # Cria o objeto TTS
    tts = gTTS(text=texto, lang='pt') 
    
    # Salva o arquivo de áudio temporário
    filename = 'voz_assistente.mp3'
    tts.save(filename)
    
    # Reproduz o áudio
    playsound(filename)
    
    # Remove o arquivo temporário
    os.remove(filename)

# ----------------------------------------------------
# 2. MÓDULO SPEECH-TO-TEXT (STT)
# ----------------------------------------------------
def ouvir_microfone():
    """
    Função que escuta o microfone, converte a fala em texto 
    e retorna o comando.
    """
    microfone = sr.Recognizer() # Inicializa o reconhecedor
    
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source) # Ajuste para ruído ambiente
        falar("Diga seu comando...")
        
        try:
            # Captura o áudio
            audio = microfone.listen(source, timeout=5, phrase_time_limit=10) 
            
            # Reconhece a fala usando a API do Google
            comando = microfone.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {comando}")
            return comando.lower() # Retorna o comando em minúsculas
            
        except sr.UnknownValueError:
            falar("Não entendi o que você disse.")
            return ""
        except sr.RequestError:
            falar("Desculpe, meu serviço de voz está indisponível.")
            return ""
        except sr.WaitTimeoutError:
            falar("Tempo esgotado. Nenhuma fala detectada.")
            return ""

# ----------------------------------------------------
# 3. MÓDULO DE FUNÇÕES AUTOMATIZADAS (Processamento de Comando)
# ----------------------------------------------------
def executar_comando(comando):
    """
    Processa o texto do comando e executa a função correspondente.
    """
    
    if "olá" in comando or "oi" in comando:
        falar("Olá! Como posso te ajudar hoje?")
        
    # REQUISITO 1: Pesquisar no Wikipedia
    elif "pesquisar por" in comando:
        falar("O que você gostaria de pesquisar no Wikipedia?")
        termo_pesquisa = ouvir_microfone()
        if termo_pesquisa:
            falar(f"Certo, pesquisando por {termo_pesquisa} no Wikipedia.")
            try:
                # Define o idioma da pesquisa
                wikipedia.set_lang("pt") 
                # Retorna o primeiro parágrafo do resultado
                resultado = wikipedia.summary(termo_pesquisa, sentences=2)
                falar(resultado)
            except wikipedia.exceptions.PageError:
                falar(f"Não encontrei informações sobre {termo_pesquisa} no Wikipedia.")
            except wikipedia.exceptions.DisambiguationError as e:
                falar(f"Seja mais específico. Opções encontradas: {e.options[:3]}") # Limita as opções
                
    # REQUISITO 2: Abrir o Youtube
    elif "abrir youtube" in comando:
        falar("Abrindo o YouTube no seu navegador.")
        webbrowser.open("https://www.youtube.com")
        
    # REQUISITO 3: Apresentar a localização da farmácia mais próxima
    elif "farmácia mais próxima" in comando or "farmácia" in comando:
        falar("Buscando por farmácias próximas no Google Maps.")
        # O comando de pesquisa usa a URL do Google Maps
        webbrowser.open("https://www.google.com/maps/search/farmácia+mais+próxima")
        
    # FUNÇÃO ADICIONAL: Contar piada
    elif "conte uma piada" in comando or "piada" in comando:
        # A biblioteca pyjokes é geralmente em inglês, mas o humor é universal!
        piada = pyjokes.get_joke(language='en', category='neutral') 
        falar("Tudo bem, lá vai uma em inglês, mas vou tentar traduzir o sentido.")
        falar(piada) 
        
    elif "hora" in comando or "horas" in comando:
        from datetime import datetime
        hora_atual = datetime.now().strftime("%H horas e %M minutos")
        falar(f"Agora são {hora_atual}")

    elif "sair" in comando or "encerrar" in comando or "tchau" in comando:
        falar("Até logo! Estarei aqui se precisar de algo.")
        return True # Sinaliza para sair do loop principal
        
    elif comando:
        falar("Desculpe, este comando não está programado. Tente algo como 'abrir youtube' ou 'pesquisar por Python'.")
        
    return False

# ----------------------------------------------------
# LOOP PRINCIPAL DO ASSISTENTE
# ----------------------------------------------------
def iniciar_assistente():
    falar("Assistente virtual inicializado. Diga 'olá' para começar ou 'sair' para finalizar.")
    
    while True:
        comando = ouvir_microfone()
        if comando:
            if executar_comando(comando):
                break

if __name__ == "__main__":
    iniciar_assistente()
