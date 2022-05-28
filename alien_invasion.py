import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    
    def __init__(self):
        pygame.init()
        
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            size = (0, 0), flags = pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        
        print(f"pygame display rect = {self.screen_rect}")
        
        print(f"bottom = {self.screen_rect.bottom}")
        print(f"bottomleft = {self.screen_rect.bottomleft}")
        print(f"bottomright = {self.screen_rect.bottomright}")
        
        print(f"midbottom = {self.screen_rect.midbottom}")
        print(f"midleft = {self.screen_rect.midleft}")
        print(f"midright = {self.screen_rect.midright}")
        print(f"midtop = {self.screen_rect.midtop}")
        
        print(f"top = {self.screen_rect.top}")
        print(f"topleft = {self.screen_rect.topleft}")
        print(f"topright = {self.screen_rect.topright}")
        
        print(f"centre = {self.screen_rect.center}")
        print(f"centerx = {self.screen_rect.centerx}")
        print(f"centery = {self.screen_rect.centery}")
        
        pygame.display.set_caption("Alien Invasion")
        
        # Set the background color
        self.bg_color = (230, 230, 230)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        
    def run_game(self):
        """start the main loop for the game."""
        while True:
            self._check_for_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        #Update  bullet position
        self.bullets.update()
        
        # Get rid of bullets that have disappeard
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
       
    def _check_for_events(self):
        """ Respond to keypresses and mouse evenets."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        
    def _check_keyup_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        pygame.display.flip()

if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
