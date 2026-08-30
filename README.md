import os 

pasta = r"C:\Users\YourUser\Downloads"

arquivos = os.listdir(pasta)

for arquivo in arquivos:
    if arquivo.endswith(".pdf"):
        print(f"Arquivo PDF encontrado: {arquivo}")

    elif arquivo.endswith(".jpg") or arquivo.endswith(".jpeg") or arquivo.endswith(".WEBP"):
        print(f"Arquivo de imagem encontrado: {arquivo}")

    elif arquivo.endswith(".txt"):
        print(f"Arquivo de texto encontrado: {arquivo}")

    elif arquivo.endswith(".docx"):
        print(f"Arquivo do Word encontrado: {arquivo}")

    elif arquivo.endswith(".xlsx"):
        print(f"Arquivo do Excel encontrado: {arquivo}")

    elif arquivo.endswith(".mp3"):
        print(f"Arquivo de áudio encontrado: {arquivo}")

    elif arquivo.endswith(".mp4"):
        print(f"Arquivo de vídeo encontrado: {arquivo}")

    elif arquivo.endswith(".zip"):
        print(f"Arquivo compactado encontrado: {arquivo}")

    elif arquivo.endswith(".rar"):
        print(f"Arquivo compactado encontrado: {arquivo}")

    elif arquivo.endswith(".exe"):
        print(f"Arquivo executável encontrado: {arquivo}")

    elif arquivo.endswith(".py"):
        print(f"Arquivo Python encontrado: {arquivo}")

    elif arquivo.endswith(".c#"):
        print(f"Arquivo C# encontrado: {arquivo}")

    else:
        print(f"Arquivo desconhecido encontrado: {arquivo}")    

    import os 
    import shutil

    pasta = r"C:\Users\YourUser\Downloads"

    arquivos = os.listdir(pasta)

    pdf = os.path.join(pasta, "PDFs")
    imagens = os.path.join(pasta, "Imagens")
    textos = os.path.join(pasta, "Textos")
    word = os.path.join(pasta, "Word")
    excel = os.path.join(pasta, "Excel")
    áudio = os.path.join(pasta, "Áudio")
    vídeo = os.path.join(pasta, "Vídeo")
    compactados = os.path.join(pasta, "Compactados")
    executáveis = os.path.join(pasta, "Executáveis")
    python = os.path.join(pasta, "Python")
    csharp = os.path.join(pasta, "C#")


    os.makedirs(pdf, exist_ok=True)
    os.makedirs(imagens, exist_ok=True)
    os.makedirs(textos, exist_ok=True)
    os.makedirs(word, exist_ok=True)
    os.makedirs(excel, exist_ok=True)
    os.makedirs(áudio, exist_ok=True)
    os.makedirs(vídeo, exist_ok=True)
    os.makedirs(compactados, exist_ok=True)
    os.makedirs(executáveis, exist_ok=True)
    os.makedirs(python, exist_ok=True)
    os.makedirs(csharp, exist_ok=True)

    for arquivo in arquivos:
        if arquivo.endswith(".pdf"):
            shutil.move(os.path.join(pasta, arquivo), os.path.join(pdf, arquivo))

        elif arquivo.endswith(".jpg") or arquivo.endswith(".jpeg") or arquivo.endswith(".WEBP"):
            shutil.move(os.path.join(pasta, arquivo), os.path.join(imagens, arquivo))

        elif arquivo.endswith(".txt"):
            shutil.move(os.path.join(pasta, arquivo), os.path.join(textos, arquivo))

        elif arquivo.endswith(".docx"):
            shutil.move(os.path.join(pasta, arquivo), os.path.join(word, arquivo))

        elif arquivo.endswith(".xlsx"):
            shutil.move(os.path.join(pasta, arquivo), os.path.join(excel, arquivo))

        elif arquivo.endswith(".mp3"):
            shutil.move(os.path.join(pasta, arquivo), os.path.join(áudio, arquivo))

        elif arquivo.endswith(".mp4"):
            shutil.move(os.path.join(pasta, arquivo), os.path.join(vídeo, arquivo))

        elif arquivo.endswith(".zip"):
            shutil.move(os.path.join(pasta, arquivo), os.path.join(compactados, arquivo))

        elif arquivo.endswith(".rar"):
            shutil.move(os.path.join(pasta, arquivo), os.path.join(compactados, arquivo))

        elif arquivo.endswith(".exe"):
            shutil.move(os.path.join(pasta, arquivo), os.path.join(executáveis, arquivo))

        elif arquivo.endswith(".py"):
            shutil.move(os.path.join(pasta, arquivo), os.path.join(python, arquivo))

        elif arquivo.endswith(".c#"):
            shutil.move(os.path.join(pasta, arquivo), os.path.join(csharp, arquivo))

print("Arquivos organizados com sucesso! Obrigado por utilizar nossos serviços")
