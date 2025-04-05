
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
config.tex_template.add_to_preamble(r"\usepackage{mathrsfs}")

class GeneratedScene(VoiceoverScene, MovingCameraScene):
    def get_final_camera_setup(self):
        self.set_speech_service(GTTSService())

        # Create all mobjects first
        title = Tex(r"Algebra of Sets", font_size=50).to_edge(UP)
        content_elements = [title]
        prev_mobject = title
    
        element0 = Tex(r""" $\Omega \rightarrow$ Space or universal set """, font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element0)
        prev_mobject = element0

        element1 = Tex(r""" $\phi \rightarrow$ Empty set """, font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element1)
        prev_mobject = element1

        element2 = Tex(r""" Class $ightarrow$ Set of sets """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element2)
        prev_mobject = element2

        element3 = Tex(r""" Collection $ightarrow$ Set of classes """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element3)
        prev_mobject = element3

        element4 = Tex(r""" Example: Let $\Omega$ be the real line $R$ and let $C_a = \{ (a,b): b > a \}$ for $a \in R$. Then $C_a$ is a class of sets for each $a$. Further $E_0 = \{ C_a: a \in R\}$ is a collection. """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element4)
        prev_mobject = element4

        element5 = Tex(r""" For any two sets $A, B \subset \Omega$, consider the relation '$A R B$ if $A \subset B$'. Then the relation '$R$' is reflexive and transitive. It is symmetric if $\Omega = \phi $. """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element5)
        prev_mobject = element5

        element6 = Tex(r""" If the index set $I$ is empty we make the convention that $\bigcup_{i \in I} E_i = \phi  \text{ and } \bigcap_{i \in I} E_i = \Omega $ """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element6)
        prev_mobject = element6

        element7 = Tex(r""" The main reason for this rather surprising convention is that the unions become larger with inclusion of more sets, whereas the intersections become smaller. For example, if $I_1$ and $I_2$ are two nonempty index sets, $I_1 \subset I_2$ then $ \bigcap_{i \in I_1} E_i \supset  \bigcap_{i \in I_2} E_i$ """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element7)
        prev_mobject = element7

        element8 = Tex(r""" Hence the smallest possible index set, i.e; $\phi$ should lead to the largest intersection, i.e; $\Omega$. """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element8)
        prev_mobject = element8

        element9 = Tex(r""" This convention is also consistent with De-Morgan's laws. """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element9)
        prev_mobject = element9

        element10 = Tex(r""" Indicator Function or Characteristic Function """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element10)
        prev_mobject = element10

        element11 = Tex(r""" $\chi_E(x) = 1$, if $x \in E$ """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element11)
        prev_mobject = element11

        element12 = Tex(r""" $\chi_E(x) = 0$, if $x \notin E$ """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element12)
        prev_mobject = element12

        element13 = Tex(r""" $E = \{x: \chi_E(x) = 1 \}$ """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element13)
        prev_mobject = element13

        element14 = Tex(r""" Clearly $\chi_{\phi} (x) = 0$ for all $x \in \Omega$ and $\chi_{\Omega} (x) = 1$ if $x \in \Omega$ """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element14)
        prev_mobject = element14

        element15 = Tex(r""" Exercises: """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element15)
        prev_mobject = element15

        element16 = Tex(r""" 1. If $A \subset B$, then $\chi_A(x) \leq \chi_B(x)$ for all $x \in \Omega$. Conversely if $\chi_A(x) \leq \chi_B(x) \forall x \in \Omega$, then $A \subset B$ """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element16)
        prev_mobject = element16

        element17 = Tex(r""" 2. $\chi_{E \cap F} (x) = \chi_E(x) \chi_F(x) = \min \{ \chi_E(x), \chi_F(x) \}$ """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element17)
        prev_mobject = element17

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
        title = Tex(r"Algebra of Sets", font_size=50).to_edge(UP)
        content_elements = [title]
        prev_mobject = title

        element0 = Tex(r""" $\Omega \rightarrow$ Space or universal set """, font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element0)
        prev_mobject = element0

        element1 = Tex(r""" $\phi \rightarrow$ Empty set """, font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element1)
        prev_mobject = element1

        element2 = Tex(r""" Class $ightarrow$ Set of sets """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element2)
        prev_mobject = element2

        element3 = Tex(r""" Collection $ightarrow$ Set of classes """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element3)
        prev_mobject = element3

        element4 = Tex(r""" Example: Let $\Omega$ be the real line $R$ and let $C_a = \{ (a,b): b > a \}$ for $a \in R$. Then $C_a$ is a class of sets for each $a$. Further $E_0 = \{ C_a: a \in R\}$ is a collection. """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element4)
        prev_mobject = element4

        element5 = Tex(r""" For any two sets $A, B \subset \Omega$, consider the relation '$A R B$ if $A \subset B$'. Then the relation '$R$' is reflexive and transitive. It is symmetric if $\Omega = \phi $. """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element5)
        prev_mobject = element5

        element6 = Tex(r""" If the index set $I$ is empty we make the convention that $\bigcup_{i \in I} E_i = \phi  \text{ and } \bigcap_{i \in I} E_i = \Omega $ """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element6)
        prev_mobject = element6

        element7 = Tex(r""" The main reason for this rather surprising convention is that the unions become larger with inclusion of more sets, whereas the intersections become smaller. For example, if $I_1$ and $I_2$ are two nonempty index sets, $I_1 \subset I_2$ then $ \bigcap_{i \in I_1} E_i \supset  \bigcap_{i \in I_2} E_i$ """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element7)
        prev_mobject = element7

        element8 = Tex(r""" Hence the smallest possible index set, i.e; $\phi$ should lead to the largest intersection, i.e; $\Omega$. """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element8)
        prev_mobject = element8

        element9 = Tex(r""" This convention is also consistent with De-Morgan's laws. """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element9)
        prev_mobject = element9

        element10 = Tex(r""" Indicator Function or Characteristic Function """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element10)
        prev_mobject = element10

        element11 = Tex(r""" $\chi_E(x) = 1$, if $x \in E$ """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element11)
        prev_mobject = element11

        element12 = Tex(r""" $\chi_E(x) = 0$, if $x \notin E$ """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element12)
        prev_mobject = element12

        element13 = Tex(r""" $E = \{x: \chi_E(x) = 1 \}$ """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element13)
        prev_mobject = element13

        element14 = Tex(r""" Clearly $\chi_{\phi} (x) = 0$ for all $x \in \Omega$ and $\chi_{\Omega} (x) = 1$ if $x \in \Omega$ """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element14)
        prev_mobject = element14

        element15 = Tex(r""" Exercises: """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element15)
        prev_mobject = element15

        element16 = Tex(r""" 1. If $A \subset B$, then $\chi_A(x) \leq \chi_B(x)$ for all $x \in \Omega$. Conversely if $\chi_A(x) \leq \chi_B(x) \forall x \in \Omega$, then $A \subset B$ """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element16)
        prev_mobject = element16

        element17 = Tex(r""" 2. $\chi_{E \cap F} (x) = \chi_E(x) \chi_F(x) = \min \{ \chi_E(x), \chi_F(x) \}$ """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element17)
        prev_mobject = element17

        # Group all elements
        content = VGroup(*content_elements)

        # Apply final camera settings before animations start
        self.camera.frame.move_to(final_center)
        self.camera.frame.set_width(final_width)

        # Animate content with voiceover
        with self.voiceover(text=r"Algebra of Sets"):
            self.play(Write(title))
            self.wait(1)

        with self.voiceover(text=r"Omega denotes the space or universal set."):
            self.play(Write(element0))
            self.wait(1)

        with self.voiceover(text=r"Phi denotes the empty set."):
            self.play(Write(element1))
            self.wait(1)

        with self.voiceover(text=r"A class is a set of sets."):
            self.play(Write(element2))
            self.wait(1)

        with self.voiceover(text=r"A collection is a set of classes."):
            self.play(Write(element3))
            self.wait(1)

        with self.voiceover(text=r"Example: Consider the real line R as the universal set. Let Ca be the set of open intervals (a, b) where b is greater than a. For each a in R, Ca is a class of sets. E0, which is the set of all such Ca's for all a in R, is a collection."):
            self.play(Write(element4))
            self.wait(1)

        with self.voiceover(text=r"If A and B are subsets of Omega, and A R B if A is a subset of B, then the relation R is reflexive and transitive. It is symmetric only if Omega is the empty set."):
            self.play(Write(element5))
            self.wait(1)

        with self.voiceover(text=r"If the index set I is empty, by convention, the union of Ei over all i in I is the empty set, and the intersection of Ei over all i in I is the universal set Omega."):
            self.play(Write(element6))
            self.wait(1)

        with self.voiceover(text=r"The reasoning behind this convention is that unions grow larger as more sets are included, while intersections shrink.  If I1 is a subset of I2, then the intersection of Ei over I1 contains the intersection of Ei over I2."):
            self.play(Write(element7))
            self.wait(1)

        with self.voiceover(text=r"Therefore, the smallest index set, which is the empty set, should result in the largest possible intersection, which is the universal set Omega."):
            self.play(Write(element8))
            self.wait(1)

        with self.voiceover(text=r"This convention aligns with De Morgan's laws."):
            self.play(Write(element9))
            self.wait(1)

        with self.voiceover(text=r"Indicator Function or Characteristic Function"):
            self.play(Write(element10))
            self.wait(1)

        with self.voiceover(text=r"The indicator function of E at x is 1 if x is an element of E."):
            self.play(Write(element11))
            self.wait(1)

        with self.voiceover(text=r"The indicator function of E at x is 0 if x is not an element of E."):
            self.play(Write(element12))
            self.wait(1)

        with self.voiceover(text=r"E is the set of all x such that the indicator function of E at x is 1."):
            self.play(Write(element13))
            self.wait(1)

        with self.voiceover(text=r"The indicator function of the empty set is 0 for all x in Omega, and the indicator function of Omega is 1 for all x in Omega."):
            self.play(Write(element14))
            self.wait(1)

        with self.voiceover(text=r"Exercises:"):
            self.play(Write(element15))
            self.wait(1)

        with self.voiceover(text=r"1. If A is a subset of B, then the indicator function of A at x is less than or equal to the indicator function of B at x for all x in Omega. Conversely, if the indicator function of A at x is less than or equal to the indicator function of B at x for all x in Omega, then A is a subset of B."):
            self.play(Write(element16))
            self.wait(1)

        with self.voiceover(text=r"2. The indicator function of the intersection of E and F at x is equal to the product of the indicator functions of E and F at x, which is also equal to the minimum of the indicator functions of E and F at x."):
            self.play(Write(element17))
            self.wait(1)

        self.wait(2)
