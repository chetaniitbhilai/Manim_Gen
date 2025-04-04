
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
config.tex_template.add_to_preamble(r"\usepackage{mathrsfs}")

class GeneratedScene(VoiceoverScene, MovingCameraScene):
    def get_final_camera_setup(self):
        self.set_speech_service(GTTSService())

        # Create all mobjects first
        title = Tex(r"Set Theory and Sequence Convergence", font_size=50).to_edge(UP)
        content_elements = [title]
        prev_mobject = title
    
        element0 = Tex(r""" Statement (a): Every point of \( X \) is in \( 0, 2 \) or \( 4 \) of the sets \( A, B, C, D \). """, font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element0)
        prev_mobject = element0

        element1 = Tex(r""" Statement (b): Similar statement holds for (b). """, font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element1)
        prev_mobject = element1

        element2 = Tex(r""" Hence \((a) \Leftrightarrow (b) \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element2)
        prev_mobject = element2

        element3 = Tex(r""" Let \( E_n = (0, 1 - \frac{1}{n}] \) if \( n \) is odd """, r""" \(= [\frac{1}{n}, 1) \) if \( n \) is even. """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element3)
        prev_mobject = element3

        element4 = Tex(r""" Then \( E_{*} = (0, 1) \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element4)
        prev_mobject = element4

        element5 = Tex(r""" Let \(\{ D_n \}\) be a sequence of sets defined by """, r""" \( D_1 = E_1, D_2 = D_1 \triangle E_2, .... \) """, r""" \( D_n = D_{n-1} \triangle E_n \) """, r""" \(n = 2, 3, ..... \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element5)
        prev_mobject = element5

        element6 = Tex(r""" Show that \(\{ D_n \}\) converges if and only if limit of the sequence \( E_n = \phi \). """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element6)
        prev_mobject = element6

        # Group all elements
        content = VGroup(*content_elements)

        # Initial camera setup with title
        self.add(title)
        title.set_opacity(0)
        self.camera.auto_zoom([title], margin=1)

        # Add content progressively with camera adjustments
        current_content = [title]
        for element in content_elements[1:]:
            self.add(element)
            element.set_opacity(0)
            current_content.append(element)

        # Final adjustment for all content
        self.play(
            self.camera.auto_zoom(
                content, margin=0.5, animate=True
            ).build(),
            run_time=2
        )

        self.camera.frame.save_state()
        self.camera.auto_zoom(content, margin=0.5)

        # Extract final camera settings
        final_center = self.camera.frame.get_center()
        final_width = self.camera.frame.get_width()

        # Restore initial camera state
        self.camera.frame.restore()

        return final_center, final_width

    def construct(self):
        final_center, final_width = self.get_final_camera_setup()

        # Create content again for the actual animation
        title = Tex(r"Set Theory and Sequence Convergence", font_size=50).to_edge(UP)
        content_elements = [title]
        prev_mobject = title

        element0 = Tex(r""" Statement (a): Every point of \( X \) is in \( 0, 2 \) or \( 4 \) of the sets \( A, B, C, D \). """, font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element0)
        prev_mobject = element0

        element1 = Tex(r""" Statement (b): Similar statement holds for (b). """, font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element1)
        prev_mobject = element1

        element2 = Tex(r""" Hence \((a) \Leftrightarrow (b) \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element2)
        prev_mobject = element2

        element3 = Tex(r""" Let \( E_n = (0, 1 - \frac{1}{n}] \) if \( n \) is odd """, r""" \(= [\frac{1}{n}, 1) \) if \( n \) is even. """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element3)
        prev_mobject = element3

        element4 = Tex(r""" Then \( E_{*} = (0, 1) \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element4)
        prev_mobject = element4

        element5 = Tex(r""" Let \(\{ D_n \}\) be a sequence of sets defined by """, r""" \( D_1 = E_1, D_2 = D_1 \triangle E_2, .... \) """, r""" \( D_n = D_{n-1} \triangle E_n \) """, r""" \(n = 2, 3, ..... \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element5)
        prev_mobject = element5

        element6 = Tex(r""" Show that \(\{ D_n \}\) converges if and only if limit of the sequence \( E_n = \phi \). """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element6)
        prev_mobject = element6

        # Group all elements
        content = VGroup(*content_elements)

        # Apply final camera settings before animations start
        self.camera.frame.move_to(final_center)
        self.camera.frame.set_width(final_width)

        # Animate content with voiceover
        with self.voiceover(text=r"Set Theory and Sequence Convergence"):
            self.play(Write(title))
            self.wait(1)

        with self.voiceover(text=r"Statement (a): Every point of X is in 0, 2, or 4 of the sets A, B, C, D."):
            self.play(Write(element0))
            self.wait(1)

        with self.voiceover(text=r"Statement (b): A similar statement holds for (b)."):
            self.play(Write(element1))
            self.wait(1)

        with self.voiceover(text=r"Hence (a) is equivalent to (b)."):
            self.play(Write(element2))
            self.wait(1)

        with self.voiceover(text=r"Let E sub n equal the interval from 0 to 1 minus 1 over n if n is odd, and equal the interval from 1 over n to 1 if n is even."):
            self.play(Write(element3))
            self.wait(1)

        with self.voiceover(text=r"Then E star, which is the limit superior of E sub n, equals the interval from 0 to 1."):
            self.play(Write(element4))
            self.wait(1)

        with self.voiceover(text=r"Let the sequence D sub n be defined by D sub 1 equals E sub 1, D sub 2 equals the symmetric difference of D sub 1 and E sub 2, and so on, such that D sub n equals the symmetric difference of D sub n minus 1 and E sub n, for n equals 2, 3, and so on."):
            self.play(Write(element5))
            self.wait(1)

        with self.voiceover(text=r"Show that the sequence D sub n converges if and only if the limit of the sequence E sub n is the empty set."):
            self.play(Write(element6))
            self.wait(1)

        self.wait(2)
