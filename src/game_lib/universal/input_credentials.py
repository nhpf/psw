import pygame
from typing import Tuple
from ..utils.math import get_center_coordinates


class InputCredentials:
    def __init__(
        self,
        screen: pygame.surface.Surface,
        clock: pygame.time.Clock,
        font: pygame.font.Font,
        fps: int,
        bg_color: Tuple[int, int, int],
    ):
        self.email = ""
        self.password = ""
        self.name = ""
        self.screen = screen
        self.clock = clock
        self.font = font
        self.fps = fps
        self.bg_color = bg_color

        button_size = (200, 50)
        button_position = get_center_coordinates(
            self.screen.get_size(), button_size[0], button_size[1]
        )
        print(button_position, button_size)
        self.ok_button = pygame.Rect(
            button_position[0],
            button_position[1] + 100,
            button_size[0],
            button_size[1],
        )

    def input_loop(self):
        num_completed_fields = 0
        while num_completed_fields < 3:
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    return None, None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if num_completed_fields == 0:
                            self.name = self.name[:-1]
                        elif num_completed_fields == 1:
                            self.email = self.email[:-1]
                        else:
                            self.password = self.password[:-1]
                    else:
                        if num_completed_fields == 0:
                            self.name += event.unicode
                        elif num_completed_fields == 1:
                            self.email += event.unicode
                        else:
                            self.password += event.unicode

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect.collidepoint(self.ok_button, pygame.mouse.get_pos()):
                        num_completed_fields += 1

            self.screen.fill(self.bg_color)

            if num_completed_fields == 0:
                text = self.font.render(f"Name: {self.name}", True, "Black")
            elif num_completed_fields == 1:
                text = self.font.render(f"Email: {self.email}", True, "Black")
            else:
                text = self.font.render(f"Password: {self.password} (+6 characters)", True, "Black")

            text_coordinates = get_center_coordinates(
                self.screen.get_size(), text.get_width(), text.get_height()
            )

            self.screen.blit(text, text_coordinates)
            pygame.draw.rect(
                self.screen, "Red", self.ok_button
            )

            ok_text = self.font.render("OK", True, "White")
            ok_coordinates = get_center_coordinates(self.screen.get_size(), ok_text.get_width(), ok_text.get_height())
            self.screen.blit(ok_text, (ok_coordinates[0], ok_coordinates[1]+100))

            pygame.display.flip()

            self.clock.tick(self.fps)

        return self.name.lower().strip(), self.email.lower().strip(), self.password.lower().strip()

