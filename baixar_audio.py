import subprocess

def baixar_audio():
    url = input("Digite a URL do vídeo do YouTube: ")
    try:
        output_file = input("Digite o nome do arquivo de saída (sem extensão): ")

        subprocess.run([
            "yt-dlp",
            "-f", "bestaudio",
            "--extract-audio",
            "--audio-format", "mp3",
            "--audio-quality", "0",
            "-o", f"{output_file}.%(ext)s",
            url
        ], check=True)
        print(f"Download concluído e arquivo salvo como {output_file}.mp3")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao processar o áudio: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    baixar_audio()
