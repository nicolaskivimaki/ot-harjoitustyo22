import os
import pygame
dirname = os.path.dirname(__file__)


class Robot(pygame.sprite.Sprite):

    """
    Robot-luokka on pygame.sprite.Sprite-aliluokka
    ja edustaa pelissä olevaa robottia/pelaajaa.
    
    """

    def __init__(self):

        """ init() alustaa robotin kuvalla, aloituspaikalla
            ja erilaisilla ominaisuuksilla, jotka 
            määrittävät sen käyttäytymisen pelissä.
        
        """
        super().__init__()
        self.rect = pygame.rect.Rect((235, 570, 30, 30))
        self.image = pygame.image.load(os.path.join(dirname, 
        "..", "assets", "robot.png"))
        self.robot = pygame.transform.smoothscale(self.image, (10, 10))
        self.rect = self.robot.get_rect()
        self.rect.x = 235
        self.rect.y = 570
        self.jump_height = 7
        self.jump_y = 570
        self.gravity = 0.15
        self.velocity = self.jump_height
        self.speed = 3
        self.jumping = True
        self.can_fall = False
        self.last_move = 0


    def handle_keys(self):

        """
        Tarkistaa näppäimmistön syötteen ja 
        kutsuu move_robot()-funktiota liikuttaakseen robottia
        vasemmalle tai oikealle.

        """

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.move_robot("l")
        if key[pygame.K_RIGHT]:
            self.move_robot("r")

    def move_robot(self, direction):

        """
        Liikuttaa robottia/pelaajaa vasemmalle tai oikealle 
        syötteen perusteella.

        """

        if direction == "l":
            self.rect.move_ip(-self.speed, 0)
        if direction == "r":
            self.rect.move_ip(self.speed, 0)

    def robot_jumping(self, first_jumps):

        """Ohjaa robotti-hyppäyskäytöstä.

        Tämä metodi päivittää robotin sijaintia y-akselilla riippuen siitä,
        onko se tällä hetkellä hyppäämässä vai putoamassa.
        
        Args:
            first_jumps: Booleani, joka osoittaa, onko robotti hypännyt 
            jostain pinnasta vielä.Handle the jumping behavior of the robot.

        """

        if first_jumps:
            if not (self.rect.y > self.jump_y):
                self.rect.y -= self.velocity
                self.last_move = self.velocity
                self.velocity -= self.gravity
            else:
                self.velocity = self.jump_height
                self.rect.y -= self.velocity
                self.last_move = self.velocity
                self.velocity -= self.gravity
        else:
            self.rect.y -= self.velocity
            self.last_move = self.velocity
            self.velocity -= self.gravity

    def start_jump(self, boost=False):

        """
        Aloittaa uuden hypyn.

        Args: 
            boost: Booleani, joka määrää onko kyseessä 
            boost-alusta vai ei.

        """
        if boost:
            self.velocity = 10
        else:
            self.velocity = self.jump_height
        self.rect.y -= self.velocity
        self.last_move = self.jump_height
        self.velocity -= self.gravity

    def get_robot_last_move(self):

        """
        Palauttaa robotin viimeisen liikkeen.

        """

        return self.last_move
    
    def get_robot_velocity(self):

        return self.velocity

    def get_robot_y(self):

        return self.rect.y

    def robot_camera_adjust(self, direction):

        self.rect.y = 335

    def draw_robot(self, surface):

        pygame.draw.rect(surface, (0, 160, 0), self.rect)
