import os
import pygame


def main() -> int:
    pygame.init()
    pygame.display.set_caption("Kota 256 Kiroween Hackathon")
    pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    auto_quit_ms = int(os.getenv("KOTA_AUTO_QUIT_MS", "0"))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        if auto_quit_ms and pygame.time.get_ticks() >= auto_quit_ms:
            running = False

        clock.tick(60)

    pygame.quit()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
