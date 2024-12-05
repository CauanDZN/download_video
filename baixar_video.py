import subprocess

def baixar_video():
    url = input("Digite a URL do vídeo do YouTube: ")
    try:
        subprocess.run(["yt-dlp", "-F", url])
        
        qualidade_video = input("\nDigite o código da qualidade de vídeo desejada: ")
        
        qualidade_audio = input("Digite o código da qualidade de áudio desejada (ou deixe em branco para usar o melhor): ")
        if not qualidade_audio:
            qualidade_audio = "bestaudio"
        
        output_file = input("\nDigite o nome do arquivo de saída (sem extensão): ")
        subprocess.run([
            "yt-dlp",
            "-f", f"{qualidade_video}+{qualidade_audio}",
            "-o", f"{output_file}.mp4",
            url
        ])
        print("Download concluído e arquivo salvo como", output_file + ".mp4")
    except Exception as e:
        print(f"Erro ao processar o vídeo: {e}")

if __name__ == "__main__":
    baixar_video()
