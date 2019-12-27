from pytube import YouTube
 
yt = YouTube('https://www.youtube.com/watch?v=OSGv2VnC0go')
titulo_video = yt.title
caption = yt.captions.get_by_language_code('pt')
legendaSRT = caption.generate_srt_captions()
 
with open(f'{titulo_video}.srt', mode='w', encoding='utf-8') as download_legenda:
    download_legenda.write(legendaSRT)
    print('Legenda salva com sucesso bb')