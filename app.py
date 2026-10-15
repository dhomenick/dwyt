# app.py
from pytubefix import YouTube

def baixar_video(url_do_usuario):
    try:
        # 1. Forçamos o uso do cliente 'MWEB' para burlar o bloqueio de streams em clipes de música
        yt = YouTube(url_do_usuario, client='MWEB')
        print(f"Tentando baixar: {yt.title}...")
        
        # 2. Primeira tentativa: Tenta pegar o vídeo padrão completo (com som e imagem)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        
        # 3. Segunda tentativa: Se o formato padrão não existir, pega a maior resolução disponível de vídeo
        if stream is None:
            print("Formato combinado indisponível. Buscando fluxo direto de alta resolução...")
            stream = yt.streams.filter(only_video=True, file_extension='mp4').order_by('resolution').desc().first()

        # 4. Executa o download se encontrar algum canal válido
        if stream is not None:
            stream.download()
            print("Download concluído com sucesso!")
            return True
        else:
            print("Erro: Nenhum formato de stream compatível foi retornado pelo YouTube.")
            return False
            
    except Exception as e:
        print(f"Erro real detalhado: {e}")
        return False
