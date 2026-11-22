from pathlib import Path
from manim import *
from mutagen.mp3 import MP3

AUDIO_DIR = Path("audio")
TARGET_DURATION = 300  # 5 minutes

class MathematicalTransformations(Scene):
    def construct(self):
        self.camera.background_color = "#0B1020"

        # Consistent visual style
        blue = "#55C7FF"
        yellow = "#FFD166"
        pink = "#FF6B9A"
        green = "#70E1A1"
        white = "#F4F7FF"

        elapsed = 0.0

        def audio_duration(filename):
            path = AUDIO_DIR / filename
            if not path.exists():
                raise FileNotFoundError(
                    f"Missing {path}. Run: python generate_voice.py"
                )
            return MP3(str(path)).info.length

        def speak_with_visual(filename, animations, visual_time=8):
            """Play one narration clip while its visual animation runs."""
            nonlocal elapsed
            duration = audio_duration(filename)
            self.add_sound(str(AUDIO_DIR / filename))
            if animations:
                self.play(
                    AnimationGroup(*animations, lag_ratio=0.15),
                    run_time=min(visual_time, duration)
                )
            remaining = duration - min(visual_time, duration)
            if remaining > 0:
                self.wait(remaining)
            elapsed += duration

        def make_triangle(color=yellow):
            tri = Polygon(
                [-1.1, -0.7, 0],
                [-0.1, 1.0, 0],
                [0.9, -0.7, 0],
                color=color,
                stroke_width=5
            )
            tri.set_fill(color, opacity=0.22)
            return tri

        # ------------------------------------------------------------
        # SCENE 1: INTRODUCTION
        # ------------------------------------------------------------
        title1 = Text("MATHEMATICAL", font_size=44, weight=BOLD, color=white)
        title2 = Text("TRANSFORMATIONS", font_size=44, weight=BOLD, color=blue)
        title = VGroup(title1, title2).arrange(DOWN, buff=0.18)
        subtitle = Text(
            "Move  •  Turn  •  Flip  •  Resize",
            font_size=25,
            color=yellow
        ).next_to(title, DOWN, buff=0.55)

        speak_with_visual(
            "scene_01.mp3",
            [Write(title), FadeIn(subtitle, shift=UP)],
            visual_time=7
        )
        self.play(FadeOut(title), FadeOut(subtitle), run_time=1)

        # ------------------------------------------------------------
        # SCENE 2: WHAT IS A TRANSFORMATION?
        # ------------------------------------------------------------
        plane = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-3.5, 3.5, 1],
            background_line_style={
                "stroke_color": "#426080",
                "stroke_opacity": 0.35,
                "stroke_width": 1
            },
            axis_config={"color": "#A9C3DF"}
        )
        plane_labels = plane.get_axis_labels(
            x_label=Text("x", font_size=24),
            y_label=Text("y", font_size=24)
        )
        original = make_triangle(yellow).shift(LEFT * 2.2)
        image = make_triangle(green).shift(RIGHT * 2.2)
        original_label = Text("PREIMAGE", font_size=22, color=yellow).next_to(original, DOWN)
        image_label = Text("IMAGE", font_size=22, color=green).next_to(image, DOWN)
        arrow = Arrow(original.get_right(), image.get_left(), color=white, buff=0.25)
        definition = Text(
            "A rule that maps a figure to a new position",
            font_size=27,
            color=white
        ).to_edge(UP)

        speak_with_visual(
            "scene_02.mp3",
            [
                Create(plane),
                FadeIn(plane_labels),
                Create(original),
                FadeIn(original_label),
                GrowArrow(arrow),
                Create(image),
                FadeIn(image_label),
                Write(definition)
            ],
            visual_time=12
        )
        self.play(
            FadeOut(plane), FadeOut(plane_labels),
            FadeOut(original), FadeOut(image),
            FadeOut(original_label), FadeOut(image_label),
            FadeOut(arrow), FadeOut(definition),
            run_time=1.2
        )

        # ------------------------------------------------------------
        # SCENE 3: TRANSLATION
        # ------------------------------------------------------------
        plane = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-3.5, 3.5, 1],
            background_line_style={"stroke_color": "#426080", "stroke_opacity": 0.35}
        )
        tri = make_triangle(yellow).move_to([-2, -0.2, 0])
        translated = tri.copy().set_color(green).set_fill(green, opacity=0.22)
        rule = MathTex(r"(x,y)\rightarrow(x+a,y+b)", color=white).scale(0.9).to_edge(UP)
        vector = Arrow(tri.get_center(), tri.get_center() + RIGHT * 3 + UP * 1.5,
                       color=pink, buff=0, stroke_width=5)
        a_label = MathTex(r"(+3,+2)", color=pink).next_to(vector, RIGHT)
        speak_with_visual(
            "scene_03.mp3",
            [
                Create(plane), Write(rule), Create(tri),
                GrowArrow(vector), FadeIn(a_label),
                Transform(tri, translated)
            ],
            visual_time=13
        )
        self.play(FadeOut(*self.mobjects), run_time=1)

        # ------------------------------------------------------------
        # SCENE 4: ROTATION
        # ------------------------------------------------------------
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-3.5, 3.5, 1],
            background_line_style={"stroke_color": "#426080", "stroke_opacity": 0.35}
        )
        tri = make_triangle(yellow).shift(RIGHT * 1.3)
        origin = Dot(ORIGIN, color=pink)
        origin_label = Text("CENTRE", font_size=19, color=pink).next_to(origin, DOWN)
        rule = MathTex(r"(x,y)\rightarrow(-y,x)", color=white).to_edge(UP)
        arc = Arc(radius=1.0, start_angle=0, angle=PI/2, color=blue).shift(LEFT * 0.1)
        speak_with_visual(
            "scene_04.mp3",
            [
                Create(plane), Write(rule), Create(tri),
                FadeIn(origin), FadeIn(origin_label), Create(arc),
                Rotate(tri, angle=PI/2, about_point=ORIGIN)
            ],
            visual_time=13
        )
        self.play(FadeOut(*self.mobjects), run_time=1)

        # ------------------------------------------------------------
        # SCENE 5: REFLECTION
        # ------------------------------------------------------------
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-3.5, 3.5, 1],
            background_line_style={"stroke_color": "#426080", "stroke_opacity": 0.35}
        )
        mirror = DashedLine(UP * 3, DOWN * 3, color=pink, stroke_width=4)
        mirror_label = Text("y-axis mirror", font_size=20, color=pink).next_to(mirror, RIGHT)
        tri = make_triangle(yellow).shift(RIGHT * 2)
        reflected = tri.copy().flip(axis=UP).shift(LEFT * 4)
        rule = MathTex(r"(x,y)\rightarrow(-x,y)", color=white).to_edge(UP)
        speak_with_visual(
            "scene_05.mp3",
            [
                Create(plane), Write(rule), Create(mirror),
                FadeIn(mirror_label), Create(tri),
                TransformFromCopy(tri, reflected)
            ],
            visual_time=12
        )
        self.play(FadeOut(*self.mobjects), run_time=1)

        # ------------------------------------------------------------
        # SCENE 6: DILATION + RECAP
        # ------------------------------------------------------------
        plane = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-3.5, 3.5, 1],
            background_line_style={"stroke_color": "#426080", "stroke_opacity": 0.35}
        )
        small = make_triangle(yellow).scale(0.65).shift(LEFT * 2)
        large = small.copy().set_color(green).set_fill(green, opacity=0.22)
        large.scale(1.8, about_point=ORIGIN)
        rule = MathTex(r"(x,y)\rightarrow(kx,ky)", color=white).to_edge(UP)
        k_label = MathTex(r"k=2", color=green).to_corner(UR).shift(DOWN * 0.8)

        speak_with_visual(
            "scene_06.mp3",
            [
                Create(plane), Write(rule), Create(small),
                FadeIn(k_label), TransformFromCopy(small, large)
            ],
            visual_time=12
        )

        recap = VGroup(
            Text("TRANSLATION  =  SLIDE", color=yellow, font_size=27),
            Text("ROTATION  =  TURN", color=blue, font_size=27),
            Text("REFLECTION  =  FLIP", color=pink, font_size=27),
            Text("DILATION  =  RESIZE", color=green, font_size=27),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).move_to(ORIGIN)

        speak_with_visual(
            "scene_07.mp3",
            [FadeOut(*self.mobjects), FadeIn(recap)],
            visual_time=5
        )

        # Pad the finished video to at least five minutes.
        # If narration itself exceeds five minutes, the video will be longer.
        if elapsed < TARGET_DURATION:
            self.wait(TARGET_DURATION - elapsed)
