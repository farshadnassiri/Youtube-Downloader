from pytubefix import YouTube
from tqdm import tqdm


class YouTubeDownloader:
    def __init__(self,url,quality="highest",output_path="."):
        self.quality=quality
        self.url=url
        self.output_path=output_path
        self.yt=YouTube(self.url,
            on_progress_callback=self.on_progress,
            on_complete_callback=self.on_complete,
        )

        self.pbar=None

    def download(self):
        try:
            if self.quality=="highest":
                video_stream = self.yt.streams.filter(progressive=True,file_extension="mp4").get_highest_resolution()
            else:
                video_stream=self.yt.streams(progressive=True,res=self.quality,file_extension="mp4").first()
            if video_stream is None:
                available_qualities=[ str(stream.resolution) for stream in self.yt.streams.filter(
                    progressive=True, file_extension="mp4")
                ]

            print(f"Title: {self.yt.title}")
            print(f"No video stream found for the given quality. Available qualities: {available_qualities}")
            return
    
            self.pbar=tqdm(total=video_stream.filesize,unit="B",unit_scale=True,desc="Downloading",leave=True)

            video_stream.download(output_path=self.output_path)
        except Exception as e:
            print(f"Error downloading video: {e}")
            if self.pbar:
                self.pbar.close()
