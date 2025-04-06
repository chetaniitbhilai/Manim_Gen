
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
config.tex_template.add_to_preamble(r"\usepackage{mathrsfs}")

class GeneratedScene(VoiceoverScene, MovingCameraScene):
    def get_final_camera_setup(self):
        self.set_speech_service(GTTSService())

        # Create all mobjects first
        title = Tex(r"Indicator Function and Limit of Sets", font_size=50).to_edge(UP)
        content_elements = [title]
        prev_mobject = title
    
        element0 = Tex(r""" Indicator Function (or Characteristic Function): """, r""" \(\chi_E(x) = \begin{cases} 1, \& \text{if } x \in E \\ 0, \& \text{if } x \notin E \end{cases}\) """, font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element0)
        prev_mobject = element0

        element1 = Tex(r""" \(E = \{x: \chi_E(x) = 1 \}\) """, font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element1)
        prev_mobject = element1

        element2 = Tex(r""" \(\chi_\phi(x) = 0\) for all \(x \in \Omega\) and \(\chi_\Omega(x) = 1\) \(\forall x \in \Omega\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element2)
        prev_mobject = element2

        element3 = Tex(r""" Exercises: """, r""" 1. If \(A \subset B\), then \(\chi_A(x) \leq \chi_B(x)\) for all \(x \in \Omega\). Conversely if \(\chi_A(x) \leq \chi_B(x)\) \(\forall\) \(x \in \Omega\), then \(A \subset B\). """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element3)
        prev_mobject = element3

        element4 = Tex(r""" 2. \(\chi_{E \cap F}(x) = \chi_E(x) \chi_F(x) = \min \{\chi_E(x) , \chi_F(x)\}\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element4)
        prev_mobject = element4

        element5 = Tex(r""" 3. \(\chi_{E \cup F}(x) = \chi_E(x) + \chi_F(x) - \chi_{E \cap F}(x) = \max \{\chi_E(x), \chi_F(x)\}\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element5)
        prev_mobject = element5

        element6 = Tex(r""" 4. \(\chi_{E^c}(x) = 1 - \chi_E(x)\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element6)
        prev_mobject = element6

        element7 = Tex(r""" 5. \(\chi_{E - F}(x) = \chi_{E \cap F^c}(x) = \chi_E(x) \chi_{F^c}(x) = \chi_E(x) (1 - \chi_F(x))\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element7)
        prev_mobject = element7

        element8 = Tex(r""" \(\Big( \bigcup_{i \in I} E_i \Big)^c = \bigcap_{i \in I} E_i^c\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element8)
        prev_mobject = element8

        element9 = Tex(r""" Let I = \(\phi\). Then the LHS = \(\phi^c = \Omega\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element9)
        prev_mobject = element9

        element10 = Tex(r""" Limit of a Sequence of Sets """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element10)
        prev_mobject = element10

        element11 = Tex(r""" Let \(\{E_n\}\) be a sequence of subsets of \(\Omega\). We define """, r""" \(E^* = \limsup E_n = \{ x \in \Omega: x \in E_n \text{ for infinitely many values of n } \}\) """, r""" and \(E_* = \liminf E_n = \{ x \in \Omega: x \in E_n \text{ for all but finitely many values of n } \}\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element11)
        prev_mobject = element11

        element12 = Tex(r""" If \(E^* = E_*\), the common value is called \(\lim E_n\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element12)
        prev_mobject = element12

        element13 = Tex(r""" In general \(E_* \subset E^*\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element13)
        prev_mobject = element13

        element14 = Tex(r""" Examples: 1. \(E_n =(0, 1-\frac{1}{n}) n = 1,2,...\) """, r""" Then \(E_* = E^* = (0,1)\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element14)
        prev_mobject = element14

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
        title = Tex(r"Indicator Function and Limit of Sets", font_size=50).to_edge(UP)
        content_elements = [title]
        prev_mobject = title

        element0 = Tex(r""" Indicator Function (or Characteristic Function): """, r""" \(\chi_E(x) = \begin{cases} 1, \& \text{if } x \in E \\ 0, \& \text{if } x \notin E \end{cases}\) """, font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element0)
        prev_mobject = element0

        element1 = Tex(r""" \(E = \{x: \chi_E(x) = 1 \}\) """, font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element1)
        prev_mobject = element1

        element2 = Tex(r""" \(\chi_\phi(x) = 0\) for all \(x \in \Omega\) and \(\chi_\Omega(x) = 1\) \(\forall x \in \Omega\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element2)
        prev_mobject = element2

        element3 = Tex(r""" Exercises: """, r""" 1. If \(A \subset B\), then \(\chi_A(x) \leq \chi_B(x)\) for all \(x \in \Omega\). Conversely if \(\chi_A(x) \leq \chi_B(x)\) \(\forall\) \(x \in \Omega\), then \(A \subset B\). """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element3)
        prev_mobject = element3

        element4 = Tex(r""" 2. \(\chi_{E \cap F}(x) = \chi_E(x) \chi_F(x) = \min \{\chi_E(x) , \chi_F(x)\}\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element4)
        prev_mobject = element4

        element5 = Tex(r""" 3. \(\chi_{E \cup F}(x) = \chi_E(x) + \chi_F(x) - \chi_{E \cap F}(x) = \max \{\chi_E(x), \chi_F(x)\}\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element5)
        prev_mobject = element5

        element6 = Tex(r""" 4. \(\chi_{E^c}(x) = 1 - \chi_E(x)\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element6)
        prev_mobject = element6

        element7 = Tex(r""" 5. \(\chi_{E - F}(x) = \chi_{E \cap F^c}(x) = \chi_E(x) \chi_{F^c}(x) = \chi_E(x) (1 - \chi_F(x))\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element7)
        prev_mobject = element7

        element8 = Tex(r""" \(\Big( \bigcup_{i \in I} E_i \Big)^c = \bigcap_{i \in I} E_i^c\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element8)
        prev_mobject = element8

        element9 = Tex(r""" Let I = \(\phi\). Then the LHS = \(\phi^c = \Omega\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element9)
        prev_mobject = element9

        element10 = Tex(r""" Limit of a Sequence of Sets """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element10)
        prev_mobject = element10

        element11 = Tex(r""" Let \(\{E_n\}\) be a sequence of subsets of \(\Omega\). We define """, r""" \(E^* = \limsup E_n = \{ x \in \Omega: x \in E_n \text{ for infinitely many values of n } \}\) """, r""" and \(E_* = \liminf E_n = \{ x \in \Omega: x \in E_n \text{ for all but finitely many values of n } \}\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element11)
        prev_mobject = element11

        element12 = Tex(r""" If \(E^* = E_*\), the common value is called \(\lim E_n\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element12)
        prev_mobject = element12

        element13 = Tex(r""" In general \(E_* \subset E^*\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element13)
        prev_mobject = element13

        element14 = Tex(r""" Examples: 1. \(E_n =(0, 1-\frac{1}{n}) n = 1,2,...\) """, r""" Then \(E_* = E^* = (0,1)\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element14)
        prev_mobject = element14

        # Group all elements
        content = VGroup(*content_elements)

        # Apply final camera settings before animations start
        self.camera.frame.move_to(final_center)
        self.camera.frame.set_width(final_width)

        # Animate content with voiceover
        with self.voiceover(text=r"Indicator Function and Limit of Sets"):
            self.play(Write(title))
            self.wait(1)

        with self.voiceover(text=r"The indicator function of a set E, denoted by chi subscript E of x, is defined as 1 if x is an element of E, and 0 if x is not an element of E."):
            self.play(Write(element0))
            self.wait(1)

        with self.voiceover(text=r"The set E can be defined as the set of all x such that the indicator function of E at x is equal to 1."):
            self.play(Write(element1))
            self.wait(1)

        with self.voiceover(text=r"The indicator function of the empty set is zero for all x in the universal set Omega, and the indicator function of the universal set Omega is one for all x in Omega."):
            self.play(Write(element2))
            self.wait(1)

        with self.voiceover(text=r"Exercise 1: If A is a subset of B, then the indicator function of A is less than or equal to the indicator function of B for all x in Omega. Conversely, if the indicator function of A is less than or equal to the indicator function of B for all x in Omega, then A is a subset of B."):
            self.play(Write(element3))
            self.wait(1)

        with self.voiceover(text=r"Exercise 2: The indicator function of the intersection of E and F is equal to the product of the indicator functions of E and F, which is also equal to the minimum of the indicator functions of E and F."):
            self.play(Write(element4))
            self.wait(1)

        with self.voiceover(text=r"Exercise 3: The indicator function of the union of E and F is equal to the sum of the indicator functions of E and F, minus the indicator function of the intersection of E and F, which is also equal to the maximum of the indicator functions of E and F."):
            self.play(Write(element5))
            self.wait(1)

        with self.voiceover(text=r"Exercise 4: The indicator function of the complement of E is equal to 1 minus the indicator function of E."):
            self.play(Write(element6))
            self.wait(1)

        with self.voiceover(text=r"Exercise 5: The indicator function of E minus F is equal to the indicator function of the intersection of E and the complement of F, which is equal to the product of the indicator function of E and the indicator function of the complement of F, which is equal to the indicator function of E multiplied by 1 minus the indicator function of F."):
            self.play(Write(element7))
            self.wait(1)

        with self.voiceover(text=r"The complement of the union of a collection of sets is equal to the intersection of the complements of those sets."):
            self.play(Write(element8))
            self.wait(1)

        with self.voiceover(text=r"Let I be the empty set. Then the left-hand side is the complement of the empty set, which equals Omega."):
            self.play(Write(element9))
            self.wait(1)

        with self.voiceover(text=r"Limit of a Sequence of Sets"):
            self.play(Write(element10))
            self.wait(1)

        with self.voiceover(text=r"Let En be a sequence of subsets of Omega. We define E star as the limit superior of En, which is the set of all x in Omega such that x is an element of En for infinitely many values of n.  And we define E subscript star as the limit inferior of En, which is the set of all x in Omega such that x is an element of En for all but finitely many values of n."):
            self.play(Write(element11))
            self.wait(1)

        with self.voiceover(text=r"If E star equals E subscript star, the common value is called the limit of En."):
            self.play(Write(element12))
            self.wait(1)

        with self.voiceover(text=r"In general, E subscript star is a subset of E star."):
            self.play(Write(element13))
            self.wait(1)

        with self.voiceover(text=r"Example: If En equals the open interval from 0 to 1 minus 1 over n, for n equals 1, 2, and so on, then E subscript star equals E star equals the open interval from 0 to 1."):
            self.play(Write(element14))
            self.wait(1)

        self.wait(2)
