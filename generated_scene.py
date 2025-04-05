
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
    
        element0 = Tex(r""" Sets, Classes, Collections """, font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element0)
        prev_mobject = element0

        element1 = Tex(r""" \(\Omega\) \(\rightarrow\) space or universal set """, font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element1)
        prev_mobject = element1

        element2 = Tex(r""" \(\phi\) \(\rightarrow\) empty set, Class \(\rightarrow\) set of sets """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element2)
        prev_mobject = element2

        element3 = Tex(r""" Collection \(\rightarrow\) set of classes """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element3)
        prev_mobject = element3

        element4 = Tex(r""" Example: Let \(\Omega\) be the real line \(\mathbb{R}\) and let \(C_{a} = \{(a,b): b > a\}\) for \(a \in \mathbb{R}\). """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element4)
        prev_mobject = element4

        element5 = Tex(r""" Then \(C_{a}\) is a class of sets for each a. """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element5)
        prev_mobject = element5

        element6 = Tex(r""" Further \(C_{0} = \{C_{a}: a \in R \}\) is a collection. """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element6)
        prev_mobject = element6

        element7 = Tex(r""" For any two sets A, B \(\subset\) \(\Omega\), consider the relation 'A R B' if A \(\subset\) B. Then the relation 'R' is reflexive and transitive. """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element7)
        prev_mobject = element7

        element8 = Tex(r""" It is symmetric if \(\Omega = \phi\). """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element8)
        prev_mobject = element8

        element9 = Tex(r""" If the index set I is empty, we make the convention that \(\bigcup_{i\in I}E_i = \phi\) and \(\bigcap_{i\in I}E_i = \Omega\). """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element9)
        prev_mobject = element9

        element10 = Tex(r""" The main reason for this rather surprising convention is that the unions become larger with inclusion of more sets, whereas the intersections become smaller. """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element10)
        prev_mobject = element10

        element11 = Tex(r""" For example, if \(I_1\) and \(I_2\) are two nonempty index sets, \(I_1 \subset I_2\) then """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element11)
        prev_mobject = element11

        element12 = Tex(r""" \(\bigcap_{i\in I_1} E_{i} \supset \bigcap_{i\in I_2} E_{i}\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element12)
        prev_mobject = element12

        element13 = Tex(r""" Hence the smallest possible index set, i.e., \(\phi\) should lead to the largest intersection, i.e., \(\Omega\). """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element13)
        prev_mobject = element13

        element14 = Tex(r""" This convention is also consistent with De-Morgan's laws. """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
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
        title = Tex(r"Algebra of Sets", font_size=50).to_edge(UP)
        content_elements = [title]
        prev_mobject = title

        element0 = Tex(r""" Sets, Classes, Collections """, font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element0)
        prev_mobject = element0

        element1 = Tex(r""" \(\Omega\) \(\rightarrow\) space or universal set """, font_size=40).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element1)
        prev_mobject = element1

        element2 = Tex(r""" \(\phi\) \(\rightarrow\) empty set, Class \(\rightarrow\) set of sets """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element2)
        prev_mobject = element2

        element3 = Tex(r""" Collection \(\rightarrow\) set of classes """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element3)
        prev_mobject = element3

        element4 = Tex(r""" Example: Let \(\Omega\) be the real line \(\mathbb{R}\) and let \(C_{a} = \{(a,b): b > a\}\) for \(a \in \mathbb{R}\). """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element4)
        prev_mobject = element4

        element5 = Tex(r""" Then \(C_{a}\) is a class of sets for each a. """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element5)
        prev_mobject = element5

        element6 = Tex(r""" Further \(C_{0} = \{C_{a}: a \in R \}\) is a collection. """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element6)
        prev_mobject = element6

        element7 = Tex(r""" For any two sets A, B \(\subset\) \(\Omega\), consider the relation 'A R B' if A \(\subset\) B. Then the relation 'R' is reflexive and transitive. """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element7)
        prev_mobject = element7

        element8 = Tex(r""" It is symmetric if \(\Omega = \phi\). """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element8)
        prev_mobject = element8

        element9 = Tex(r""" If the index set I is empty, we make the convention that \(\bigcup_{i\in I}E_i = \phi\) and \(\bigcap_{i\in I}E_i = \Omega\). """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element9)
        prev_mobject = element9

        element10 = Tex(r""" The main reason for this rather surprising convention is that the unions become larger with inclusion of more sets, whereas the intersections become smaller. """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element10)
        prev_mobject = element10

        element11 = Tex(r""" For example, if \(I_1\) and \(I_2\) are two nonempty index sets, \(I_1 \subset I_2\) then """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element11)
        prev_mobject = element11

        element12 = Tex(r""" \(\bigcap_{i\in I_1} E_{i} \supset \bigcap_{i\in I_2} E_{i}\) """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element12)
        prev_mobject = element12

        element13 = Tex(r""" Hence the smallest possible index set, i.e., \(\phi\) should lead to the largest intersection, i.e., \(\Omega\). """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element13)
        prev_mobject = element13

        element14 = Tex(r""" This convention is also consistent with De-Morgan's laws. """, font_size=36).next_to(prev_mobject, DOWN, buff=0.5)
        content_elements.append(element14)
        prev_mobject = element14

        # Group all elements
        content = VGroup(*content_elements)

        # Apply final camera settings before animations start
        self.camera.frame.move_to(final_center)
        self.camera.frame.set_width(final_width)

        # Animate content with voiceover
        with self.voiceover(text=r"Algebra of Sets"):
            self.play(Write(title))
            self.wait(1)

        with self.voiceover(text=r"Sets, Classes, Collections"):
            self.play(Write(element0))
            self.wait(1)

        with self.voiceover(text=r"Omega represents the space or universal set."):
            self.play(Write(element1))
            self.wait(1)

        with self.voiceover(text=r"Phi represents the empty set, and a Class is a set of sets."):
            self.play(Write(element2))
            self.wait(1)

        with self.voiceover(text=r"A Collection is a set of classes."):
            self.play(Write(element3))
            self.wait(1)

        with self.voiceover(text=r"Example: Let Omega be the real line R, and let C sub a equal the set of open intervals from a to b, where b is greater than a, for a in R."):
            self.play(Write(element4))
            self.wait(1)

        with self.voiceover(text=r"Then C sub a is a class of sets for each a."):
            self.play(Write(element5))
            self.wait(1)

        with self.voiceover(text=r"Further, C sub 0, equal to the set of C sub a, where a is in R, is a collection."):
            self.play(Write(element6))
            self.wait(1)

        with self.voiceover(text=r"For any two sets A and B, which are subsets of Omega, consider the relation A R B, if A is a subset of B. Then the relation R is reflexive and transitive."):
            self.play(Write(element7))
            self.wait(1)

        with self.voiceover(text=r"It is symmetric if Omega equals the empty set."):
            self.play(Write(element8))
            self.wait(1)

        with self.voiceover(text=r"If the index set I is empty, we make the convention that the union of E sub i over all i in I equals the empty set, and the intersection of E sub i over all i in I equals Omega."):
            self.play(Write(element9))
            self.wait(1)

        with self.voiceover(text=r"The main reason for this rather surprising convention is that the unions become larger with inclusion of more sets, whereas the intersections become smaller."):
            self.play(Write(element10))
            self.wait(1)

        with self.voiceover(text=r"For example, if I one and I two are two nonempty index sets, and I one is a subset of I two, then:"):
            self.play(Write(element11))
            self.wait(1)

        with self.voiceover(text=r"The intersection of E sub i over all i in I one contains the intersection of E sub i over all i in I two."):
            self.play(Write(element12))
            self.wait(1)

        with self.voiceover(text=r"Hence the smallest possible index set, that is, phi, should lead to the largest intersection, that is, Omega."):
            self.play(Write(element13))
            self.wait(1)

        with self.voiceover(text=r"This convention is also consistent with De-Morgan's laws."):
            self.play(Write(element14))
            self.wait(1)

        self.wait(2)
