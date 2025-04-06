
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
config.tex_template.add_to_preamble(r"\usepackage{mathrsfs}")

class GeneratedScene(VoiceoverScene, MovingCameraScene):
    def get_final_camera_setup(self):
        self.set_speech_service(GTTSService())

        # Create all mobjects first
        title = Tex(r"Indicator Function or Characteristic Function", font_size=50).to_edge(UP)
        content_elements = [title]
        prev_mobject = title
    
        element0 = Tex(r""" \(\chi_{E}(x) = 1, \quad \) if \( x \in E \) """, r""" \(\chi_{E}(x) = 0, \quad \) if \( x \notin E \) """, r""" We have \( E = \{ x : \chi_E(x) = 1\} \). """, font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element0)
        prev_mobject = element0

        element1 = Tex(r""" \(\chi_{\phi}(x) = 0 \quad \) for all \( x \in \Omega \) """, r""" \(\chi_{\Omega}(x) = 1 \quad \) if \( x \in \Omega \) """, font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element1)
        prev_mobject = element1

        element2 = Tex(r""" 1. If \(A \subset B\), then \(\chi_{A}(x) \leq \chi_{B}(x)\) for all \(x \in \Omega\). Conversely if \(\chi_{A}(x) \leq \chi_{B}(x) \) for all \( x \in \Omega\), then \(A \subset B\). """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element2)
        prev_mobject = element2

        element3 = Tex(r""" 2. \(\chi_{E \cap F}(x) = \chi_{E}(x) \cdot \chi_{F}(x) = \min \{\chi_{E}(x), \chi_{F}(x)\} \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element3)
        prev_mobject = element3

        element4 = Tex(r""" \(\chi_{E \cup F}(x) = \chi_{E}(x) + \chi_{F}(x) - \chi_{E \cap F}(x) \) """, r""" \(=\max\{\chi_{E}(x), \chi_{F}(x)\} \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element4)
        prev_mobject = element4

        element5 = Tex(r""" \(\chi_{E^{c}}(x) = 1 - \chi_{E}(x) \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element5)
        prev_mobject = element5

        element6 = Tex(r""" \(\chi_{E - F}(x) = \chi_{E \cap F^{c}} (x) = \chi_{E}(x) \cdot \chi_{F^{c}}(x) \) """, r""" \(= \chi_{E}(x) \cdot (1 - \chi_{F}(x)) \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element6)
        prev_mobject = element6

        element7 = Tex(r""" \(\left( \bigcup_{i \in I} E_{i}\right)^{c} = \bigcap_{i \in I} E_{i}^{c} \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element7)
        prev_mobject = element7

        element8 = Tex(r""" Let \(I = \phi\). Then the LHS = \(\phi^{c} = X \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element8)
        prev_mobject = element8

        element9 = Tex(r""" max \(\chi_{E}(x)\), \(\chi_{F}(x)\) = 0 then both \(\chi_{E}(x) \) \& \(\chi_{F}(x)\) must be zero """, r""" Hence \(\chi_{E \cup F}(x) = 0 \) """, r""" If maximum value is 1 then either one or both of \(\chi_{E}\) """, r"""  \(\chi_{F}\) must be 1 and so \(\chi_{E \cup F}\) will also 1 """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element9)
        prev_mobject = element9

        element10 = Tex(r""" Limit of a Sequence of Sets """, r""" Let \(\{ E_{n} \}\) be a sequence of subsets of \(\Omega\). We define """, r""" \(E^{*} = \limsup E_{n} \) """, r""" \(= \{ x \in \Omega : x \in E_{n} \) for infinitely many values of n \} """, r""" and """, r""" \(E_{*} = \liminf E_{n} \) """, r""" \(= \{ x \in \Omega : x \in E_{n} \) for all but finitely many values of n \} """, r""" If \( E^{*} = E_{*} \), the common value is called \( \lim E_{n} \) """, r""" In general \( E_{*} \subset E^{*} \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element10)
        prev_mobject = element10

        element11 = Tex(r""" Examples : """, r""" \(E_{n} = (0, 1 - \frac{1}{n}) \quad n = 1, 2, \dots \) """, r""" Then \( E_{*} = E^{*} = (0, 1) \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element11)
        prev_mobject = element11

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
        title = Tex(r"Indicator Function or Characteristic Function", font_size=50).to_edge(UP)
        content_elements = [title]
        prev_mobject = title

        element0 = Tex(r""" \(\chi_{E}(x) = 1, \quad \) if \( x \in E \) """, r""" \(\chi_{E}(x) = 0, \quad \) if \( x \notin E \) """, r""" We have \( E = \{ x : \chi_E(x) = 1\} \). """, font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element0)
        prev_mobject = element0

        element1 = Tex(r""" \(\chi_{\phi}(x) = 0 \quad \) for all \( x \in \Omega \) """, r""" \(\chi_{\Omega}(x) = 1 \quad \) if \( x \in \Omega \) """, font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element1)
        prev_mobject = element1

        element2 = Tex(r""" 1. If \(A \subset B\), then \(\chi_{A}(x) \leq \chi_{B}(x)\) for all \(x \in \Omega\). Conversely if \(\chi_{A}(x) \leq \chi_{B}(x) \) for all \( x \in \Omega\), then \(A \subset B\). """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element2)
        prev_mobject = element2

        element3 = Tex(r""" 2. \(\chi_{E \cap F}(x) = \chi_{E}(x) \cdot \chi_{F}(x) = \min \{\chi_{E}(x), \chi_{F}(x)\} \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element3)
        prev_mobject = element3

        element4 = Tex(r""" \(\chi_{E \cup F}(x) = \chi_{E}(x) + \chi_{F}(x) - \chi_{E \cap F}(x) \) """, r""" \(=\max\{\chi_{E}(x), \chi_{F}(x)\} \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element4)
        prev_mobject = element4

        element5 = Tex(r""" \(\chi_{E^{c}}(x) = 1 - \chi_{E}(x) \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element5)
        prev_mobject = element5

        element6 = Tex(r""" \(\chi_{E - F}(x) = \chi_{E \cap F^{c}} (x) = \chi_{E}(x) \cdot \chi_{F^{c}}(x) \) """, r""" \(= \chi_{E}(x) \cdot (1 - \chi_{F}(x)) \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element6)
        prev_mobject = element6

        element7 = Tex(r""" \(\left( \bigcup_{i \in I} E_{i}\right)^{c} = \bigcap_{i \in I} E_{i}^{c} \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element7)
        prev_mobject = element7

        element8 = Tex(r""" Let \(I = \phi\). Then the LHS = \(\phi^{c} = X \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element8)
        prev_mobject = element8

        element9 = Tex(r""" max \(\chi_{E}(x)\), \(\chi_{F}(x)\) = 0 then both \(\chi_{E}(x) \) \& \(\chi_{F}(x)\) must be zero """, r""" Hence \(\chi_{E \cup F}(x) = 0 \) """, r""" If maximum value is 1 then either one or both of \(\chi_{E}\) """, r"""  \(\chi_{F}\) must be 1 and so \(\chi_{E \cup F}\) will also 1 """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element9)
        prev_mobject = element9

        element10 = Tex(r""" Limit of a Sequence of Sets """, r""" Let \(\{ E_{n} \}\) be a sequence of subsets of \(\Omega\). We define """, r""" \(E^{*} = \limsup E_{n} \) """, r""" \(= \{ x \in \Omega : x \in E_{n} \) for infinitely many values of n \} """, r""" and """, r""" \(E_{*} = \liminf E_{n} \) """, r""" \(= \{ x \in \Omega : x \in E_{n} \) for all but finitely many values of n \} """, r""" If \( E^{*} = E_{*} \), the common value is called \( \lim E_{n} \) """, r""" In general \( E_{*} \subset E^{*} \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element10)
        prev_mobject = element10

        element11 = Tex(r""" Examples : """, r""" \(E_{n} = (0, 1 - \frac{1}{n}) \quad n = 1, 2, \dots \) """, r""" Then \( E_{*} = E^{*} = (0, 1) \) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element11)
        prev_mobject = element11

        # Group all elements
        content = VGroup(*content_elements)

        # Apply final camera settings before animations start
        self.camera.frame.move_to(final_center)
        self.camera.frame.set_width(final_width)

        # Animate content with voiceover
        with self.voiceover(text=r"Indicator Function or Characteristic Function"):
            self.play(Write(title))
            self.wait(1)

        with self.voiceover(text=r"The indicator function of set E, denoted chi sub E of x, is equal to 1 if x is in E, and 0 if x is not in E."):
            self.play(Write(element0))
            self.wait(1)

        with self.voiceover(text=r"The indicator function of the empty set is 0 for all x in Omega."):
            self.play(Write(element1))
            self.wait(1)

        with self.voiceover(text=r"If A is a subset of B, then the indicator function of A is less than or equal to the indicator function of B for all x in Omega."):
            self.play(Write(element2))
            self.wait(1)

        with self.voiceover(text=r"The indicator function of the intersection of E and F is equal to the product of the indicator functions of E and F, which is also equal to the minimum of the indicator functions of E and F."):
            self.play(Write(element3))
            self.wait(1)

        with self.voiceover(text=r"The indicator function of the union of E and F is equal to the sum of the indicator functions of E and F minus the indicator function of the intersection of E and F."):
            self.play(Write(element4))
            self.wait(1)

        with self.voiceover(text=r"The indicator function of the complement of E is equal to 1 minus the indicator function of E."):
            self.play(Write(element5))
            self.wait(1)

        with self.voiceover(text=r"The indicator function of E minus F is equal to the indicator function of the intersection of E and the complement of F."):
            self.play(Write(element6))
            self.wait(1)

        with self.voiceover(text=r"The complement of the union of E sub i over all i in I is equal to the intersection of the complements of E sub i over all i in I."):
            self.play(Write(element7))
            self.wait(1)

        with self.voiceover(text=r"Let I be the empty set. Then the left hand side is the complement of the empty set, which is equal to X (Omega)."):
            self.play(Write(element8))
            self.wait(1)

        with self.voiceover(text=r"If the maximum of the indicator functions of E and F is 0, then both indicator functions of E and F must be zero."):
            self.play(Write(element9))
            self.wait(1)

        with self.voiceover(text=r"Let's define the limit of a sequence of sets."):
            self.play(Write(element10))
            self.wait(1)

        with self.voiceover(text=r"Here is an example."):
            self.play(Write(element11))
            self.wait(1)

        self.wait(2)
