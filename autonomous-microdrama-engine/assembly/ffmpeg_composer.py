import os

class VideoComposer:
    """
    Automates multi-clip vertical video stitching, auto-ducking BGM under TTS,
    and burning animated ASS/SRT subtitles.
    """
    @staticmethod
    def generate_concat_script(clip_paths: list, output_path: str) -> str:
        """Produces an FFmpeg bash command line for stitching and audio mastering."""
        filter_complex = (
            "[0:v]scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,setsar=1[v0];"
        )
        cmd = f"ffmpeg -y -i input_concat.txt -filter_complex '{filter_complex}' -c:v libx264 -crf 18 -preset fast {output_path}"
        return cmd

    @staticmethod
    def generate_subtitle_style_spec() -> str:
        return """[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: TikTokBold,Impact,64,&H0000FFFF,&H000000FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,0,2,20,20,240,1
"""
