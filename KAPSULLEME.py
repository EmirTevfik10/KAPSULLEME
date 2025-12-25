import pygame
import sys
import random
import os

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)
DARK_BLUE = (10, 20, 40)
NAVY = (20, 30, 60)
GRID_COLOR = (30, 45, 80)
CYAN = (0, 255, 255)
PURPLE = (147, 51, 234)
PINK = (236, 72, 153)
BUTTON_COLOR = (40, 60, 100)
BUTTON_HOVER = (60, 90, 140)
GREEN = (50, 220, 50)
RED = (220, 50, 50)
YELLOW = (250, 204, 21)
LIGHT_GRAY = (180, 180, 190)
ORANGE = (255, 165, 0)

PLAYER1_COLOR = (52, 211, 153)
PLAYER2_COLOR = (251, 146, 60)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Kapsülleme - OSI Eşleştirme Oyunu")

clock = pygame.time.Clock()

try:
    TITLE_FONT = pygame.font.SysFont('Arial', 120, bold=True)
    SUBTITLE_FONT = pygame.font.SysFont('Arial', 48, bold=True)
    BUTTON_FONT = pygame.font.SysFont('Arial', 42, bold=True)
    SMALL_FONT = pygame.font.SysFont('Arial', 32)
    SYMBOL_FONT = pygame.font.SysFont('Arial', 50, bold=True)
except:
    TITLE_FONT = pygame.font.Font(None, 120)
    SUBTITLE_FONT = pygame.font.Font(None, 48)
    BUTTON_FONT = pygame.font.Font(None, 42)
    SMALL_FONT = pygame.font.Font(None, 32)
    SYMBOL_FONT = pygame.font.Font(None, 50)

LEVELS = {
    1: {
        "name": "Seviye 1 - OSI Katman Numaraları",
        "description": "Bu seviyede Layer numaralarını katman isimleriyle eşleştireceksiniz.",
        "pairs": {
            "Layer 1": "Fiziksel Katman",
            "Layer 2": "Veri Bagi Katmani",
            "Layer 3": "Ag Katmani",
            "Layer 4": "Tasima Katmani",
            "Layer 5": "Oturum Katmani",
            "Layer 6": "Sunum Katmani",
            "Layer 7": "Uygulama Katmani"
        },
        "images": {
            "Layer 1": "cards/level1/layer1.png",
            "Layer 2": "cards/level1/layer2.png",
            "Layer 3": "cards/level1/layer3.png",
            "Layer 4": "cards/level1/layer4.png",
            "Layer 5": "cards/level1/layer5.png",
            "Layer 6": "cards/level1/layer6.png",
            "Layer 7": "cards/level1/layer7.jpg",
            "Fiziksel Katman": "cards/level1/fiziksel.png",
            "Veri Bagi Katmani": "cards/level1/veri_bagi.png",
            "Ag Katmani": "cards/level1/ag.png",
            "Tasima Katmani": "cards/level1/tasima.png",
            "Oturum Katmani": "cards/level1/oturum.png",
            "Sunum Katmani": "cards/level1/sunum.png",
            "Uygulama Katmani": "cards/level1/uygulama.png"
        }
    },
    2: {
        "name": "Seviye 2 - Port ve Protokol Eşleştirme",
        "description": "Bu seviyede port numaralarını ait oldukları protokollerle eşleştireceksiniz.",
        "pairs": {
            "Port 20": "FTP Data",
            "Port 21": "FTP Command",
            "Port 23": "Telnet",
            "Port 25": "SMTP",
            "Port 80": "HTTP",
            "Port 110": "POP3",
            "Port 443": "HTTPS"
        },
        "images": {
            "Port 20": "cards/level2/port20.jpeg",
            "Port 21": "cards/level2/port21.jpeg",
            "Port 23": "cards/level2/port23.png",
            "Port 25": "cards/level2/port25.jpeg",
            "Port 80": "cards/level2/port80.jpeg",
            "Port 110": "cards/level2/port110.jpeg",
            "Port 443": "cards/level2/port443.jpeg",
            "FTP Data": "cards/level2/ftpdata.jpeg",
            "FTP Command": "cards/level2/ftpcommand.jpeg",
            "Telnet": "cards/level2/telnet.png",
            "SMTP": "cards/level2/smtp.jpeg",
            "HTTP": "cards/level2/http.jpeg",
            "POP3": "cards/level2/pop3.jpeg",
            "HTTPS": "cards/level2/HTTPS.png"
        }
    },
    3: {
        "name": "Seviye 3 - Gelişmiş Ağ Donanımları",
        "description": "Tüm katmanlardaki cihazları ve donanımları eşleştirin.",
        "pairs": {
            "Hub": "Fiziksel Katman (L1)",
            "Switch (Anahtar)": "Veri Bagi Katmani (L2)",
            "Router (Yonlendirici)": "Ag Katmani (L3)",
            "L3 Switch": "Ag Katmani (L3)",
            "Guvenlik Duvari (Firewall)": "Tasima Katmani (L4)",
            "Proxy Sunucu": "Uygulama Katmani (L7)",
            "Kablo (Ethernet)": "Fiziksel Katman (L1)",
            "Bridge (Kopru)": "Veri Bagi Katmani (L2)",
            "Access Point (WAP)": "Veri Bagi Katmani (L2)",
        },
        "images": {
            "Hub": "cards/level3/hub.png",
            "Switch (Anahtar)": "cards/level3/switch.png",
            "Router (Yonlendirici)": "cards/level3/router.png",
            "L3 Switch": "cards/level3/l3switch.png",
            "Guvenlik Duvari (Firewall)": "cards/level3/firewall.png",
            "Proxy Sunucu": "cards/level3/proxy.png",
            "Kablo (Ethernet)": "cards/level3/cable.png",
            "Bridge (Kopru)": "cards/level3/bridge.png",
            "Access Point (WAP)": "cards/level3/accesspoint.png",
            "Fiziksel Katman (L1)": "cards/level3/fiziksel.png",
            "Veri Bagi Katmani (L2)": "cards/level3/veri_bagi.png",
            "Ag Katmani (L3)": "cards/level3/ag.png",
            "Tasima Katmani (L4)": "cards/level3/tasima.png",
            "Oturum Katmani (L5)": "cards/level3/oturum.png",
            "Sunum Katmani (L6)": "cards/level3/sunum.png",
            "Uygulama Katmani (L7)": "cards/level3/uygulama.png"
        }
    }
}

try:
    logo_image = pygame.image.load("logo.png").convert_alpha()
    logo_width = 400
    logo_height = int(logo_image.get_height() * (logo_width / logo_image.get_width()))
    logo_image = pygame.transform.smoothscale(logo_image, (logo_width, logo_height))
    logo_loaded = True
except:
    print("UYARI: logo.png bulunamadı. Dekoratif logo kullanılıyor.")
    logo_loaded = False

class GameCard:
    def __init__(self, text, x, y, width, height, match_key, image_path=None):
        self.text = text
        self.match_key = match_key
        self.rect = pygame.Rect(x, y, width, height) 
        self.original_pos = (x, y)
        self.dragging = False
        self.matched = False
        self.hover = False
        self.offset_x = 0
        self.offset_y = 0
        self.image = None
        self.image_path = image_path
        self.matched_by = None

        if image_path and os.path.exists(image_path):
            try:
                img = pygame.image.load(image_path).convert_alpha()
                iw, ih = img.get_width(), img.get_height()
                cw = width
                ch = int((cw / iw) * ih)
                self.rect = pygame.Rect(x, y, cw, ch)
                new_w = cw
                new_h = ch
                img = pygame.transform.smoothscale(img, (new_w, new_h))
                self.image = pygame.Surface((cw, ch), pygame.SRCALPHA)
                self.image.fill((0, 0, 0, 0))
                self.image.blit(img, (0, 0))
            except Exception as e:
                print(f"UYARI: {image_path} yüklenemedi: {e}")
                self.image = None
    
    def draw(self, surface):
        if self.matched:
            border_color = PLAYER1_COLOR if self.matched_by == 1 else PLAYER2_COLOR
            border_width = 5
        elif self.hover or self.dragging:
            border_color = CYAN
            border_width = 4
        else:
            border_color = (100, 120, 160)
            border_width = 3
        
        if self.image:
            surface.blit(self.image, self.rect)
            pygame.draw.rect(surface, border_color, self.rect, border_width, border_radius=12)
        else:
            if self.matched:
                color = (20, 80, 20)
            elif self.hover or self.dragging:
                color = BUTTON_HOVER
            else:
                color = BUTTON_COLOR
            
            pygame.draw.rect(surface, color, self.rect, border_radius=12)
            pygame.draw.rect(surface, border_color, self.rect, border_width, border_radius=12)
            
            words = self.text.split()
            lines = []
            current_line = []
            
            for word in words:
                test_line = current_line + [word]
                test_text = " ".join(test_line)
                if BUTTON_FONT.size(test_text)[0] < self.rect.width - 30:
                    current_line.append(word)
                else:
                    if current_line:
                        lines.append(" ".join(current_line))
                    current_line = [word]
            
            if current_line:
                lines.append(" ".join(current_line))
            
            total_height = len(lines) * BUTTON_FONT.get_height()
            start_y = self.rect.centery - total_height // 2
            
            for i, line in enumerate(lines):
                text_obj = BUTTON_FONT.render(line, True, WHITE)
                text_rect = text_obj.get_rect(center=(self.rect.centerx, start_y + i * BUTTON_FONT.get_height()))
                surface.blit(text_obj, text_rect)
        
        if self.matched:
            check_size = 40
            check_x = self.rect.right - check_size - 10
            check_y = self.rect.top + 10
            check_color = PLAYER1_COLOR if self.matched_by == 1 else PLAYER2_COLOR
            pygame.draw.circle(surface, check_color, (check_x, check_y), check_size // 2)
            pygame.draw.circle(surface, WHITE, (check_x, check_y), check_size // 2, 3)
            # Unicode tick yerine basit bir çizim
            pygame.draw.line(surface, WHITE, (check_x - 8, check_y), (check_x - 3, check_y + 8), 3)
            pygame.draw.line(surface, WHITE, (check_x - 3, check_y + 8), (check_x + 8, check_y - 8), 3)
    
    def update_hover(self, mouse_pos):
        if not self.matched:
            self.hover = self.rect.collidepoint(mouse_pos)
    
    def start_drag(self, mouse_pos):
        if not self.matched and self.rect.collidepoint(mouse_pos):
            self.dragging = True
            self.offset_x = self.rect.x - mouse_pos[0]
            self.offset_y = self.rect.y - mouse_pos[1]
            return True
        return False
    
    def drag(self, mouse_pos):
        if self.dragging:
            self.rect.x = mouse_pos[0] + self.offset_x
            self.rect.y = mouse_pos[1] + self.offset_y
    
    def stop_drag(self):
        self.dragging = False
    
    def snap_back(self):
        self.rect.topleft = self.original_pos

# Helper functions
def draw_gradient_background():
    for y in range(SCREEN_HEIGHT):
        ratio = y / SCREEN_HEIGHT
        r = int(DARK_BLUE[0] * (1 - ratio) + BLACK[0] * ratio)
        g = int(DARK_BLUE[1] * (1 - ratio) + BLACK[1] * ratio)
        b = int(DARK_BLUE[2] * (1 - ratio) + BLACK[2] * ratio)
        pygame.draw.line(screen, (r, g, b), (0, y), (SCREEN_WIDTH, y))
    
    grid_spacing = 50
    for x in range(0, SCREEN_WIDTH, grid_spacing):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT), 1)
    for y in range(0, SCREEN_HEIGHT, grid_spacing):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y), 1)

def draw_text(text, font, color, x, y, center=True):
    text_surface = font.render(text, True, color)
    if center:
        text_rect = text_surface.get_rect(center=(x, y))
    else:
        text_rect = text_surface.get_rect(topleft=(x, y))
    screen.blit(text_surface, text_rect)
    return text_rect

def draw_button(rect, text, mouse_pos):
    is_hover = rect.collidepoint(mouse_pos)
    color = BUTTON_HOVER if is_hover else BUTTON_COLOR
    
    pygame.draw.rect(screen, color, rect, border_radius=15)
    
    if is_hover:
        pygame.draw.rect(screen, CYAN, rect, 3, border_radius=15)
    else:
        pygame.draw.rect(screen, (100, 120, 160), rect, 2, border_radius=15)
    
    draw_text(text, BUTTON_FONT, WHITE, rect.centerx, rect.centery)
    
    return is_hover

def draw_logo():
    center_x = SCREEN_WIDTH // 2
    start_y = 180
    layer_height = 25
    
    colors = [
        (239, 68, 68),
        (249, 115, 22),
        (250, 204, 21),
        (34, 197, 94),
        (6, 182, 212),
        (59, 130, 246),
        (147, 51, 234)
    ]
    
    for i, color in enumerate(colors):
        width = 600 - (i * 40)
        rect = pygame.Rect(center_x - width//2, start_y + i * (layer_height + 5), width, layer_height)
        pygame.draw.rect(screen, color, rect, border_radius=8)
        pygame.draw.rect(screen, WHITE, rect, 2, border_radius=8)
        
        layer_num = 7 - i
        num_text = SMALL_FONT.render(f"L{layer_num}", True, WHITE)
        screen.blit(num_text, (rect.x + 10, rect.centery - num_text.get_height()//2))


def main_menu():
    running = True
    credits_acik = False

    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if credits_acik:
                        credits_acik = False
                    else:
                        return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if credits_acik:
                        if close_button_rect.collidepoint(mouse_pos):
                            credits_acik = False
                    else:
                        if play_button.collidepoint(mouse_pos):
                            return "play"
                        if exit_button.collidepoint(mouse_pos):
                            return "quit"
                        if credits_button.collidepoint(mouse_pos):
                            credits_acik = True

        draw_gradient_background()

        if logo_loaded:
            logo_x = SCREEN_WIDTH // 2 - logo_image.get_width() // 2
            logo_y = 250
            screen.blit(logo_image, (logo_x, logo_y))
        else:
            draw_logo()

        draw_text("Kapsülleme - OSI Eşleştirme Oyunu", SUBTITLE_FONT, WHITE, SCREEN_WIDTH // 2, 80)

        center_x = SCREEN_WIDTH // 2
        button_y = 600
        button_width = 400
        button_height = 80
        button_spacing = 100

        play_button = pygame.Rect(center_x - button_width // 2, button_y, button_width, button_height)
        exit_button = pygame.Rect(center_x - button_width // 2, button_y + button_spacing, button_width, button_height)

        credits_button_width = 400
        credits_button_height = 70
        credits_button_padding = 40
        credits_button = pygame.Rect(
            credits_button_padding,
            SCREEN_HEIGHT - credits_button_height - credits_button_padding,
            credits_button_width,
            credits_button_height
        )

        if not credits_acik:
            draw_button(play_button, ">> OYNA", mouse_pos)
            draw_button(exit_button, "X ÇIKIŞ", mouse_pos)
            draw_button(credits_button, "HAZIRLAYANLAR", mouse_pos)

        if credits_acik:
            close_button_rect = draw_credits_popup(mouse_pos)

        draw_text("ESC - Cıkış", SMALL_FONT, GRID_COLOR, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

        pygame.display.flip()
        clock.tick(60)

    return "quit"

def game_mode_screen():
    running = True
    
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit", None
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu", None
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if single_button.collidepoint(mouse_pos):
                        return "game", 1
                    if multi_button.collidepoint(mouse_pos):
                        return "game", 2
                    if back_button.collidepoint(mouse_pos):
                        return "menu", None
        
        draw_gradient_background()
        
        draw_text("OYUN MODU SEC", TITLE_FONT, CYAN, SCREEN_WIDTH//2, 250)
        
        center_x = SCREEN_WIDTH // 2
        button_y = 450
        button_width = 500
        button_height = 100
        button_spacing = 130
        
        single_button = pygame.Rect(center_x - button_width//2, button_y, button_width, button_height)
        multi_button = pygame.Rect(center_x - button_width//2, button_y + button_spacing, button_width, button_height)
        back_button = pygame.Rect(center_x - button_width//2, button_y + button_spacing * 2, button_width, button_height)
        
        draw_button(single_button, "TEK OYUNCULU", mouse_pos)
        draw_button(multi_button, "IKI OYUNCULU", mouse_pos)
        draw_button(back_button, "<< GERI", mouse_pos)
        
        draw_text("ESC - Geri", SMALL_FONT, GRID_COLOR, SCREEN_WIDTH//2, SCREEN_HEIGHT - 50)
        
        pygame.display.flip()
        clock.tick(60)
    
    return "quit", None

def show_pause_menu():
    running = True
    
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "resume"
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if resume_button.collidepoint(mouse_pos):
                    return "resume"
                if menu_button.collidepoint(mouse_pos):
                    return "menu"
                if quit_button.collidepoint(mouse_pos):
                    return "quit"
        
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        draw_text("OYUN DURAKLATILDI", TITLE_FONT, CYAN, SCREEN_WIDTH // 2, 250)
        
        center_x = SCREEN_WIDTH // 2
        button_width = 500
        button_height = 90
        button_spacing = 110
        start_y = 450
        
        resume_button = pygame.Rect(center_x - button_width // 2, start_y, button_width, button_height)
        menu_button = pygame.Rect(center_x - button_width // 2, start_y + button_spacing, button_width, button_height)
        quit_button = pygame.Rect(center_x - button_width // 2, start_y + button_spacing * 2, button_width, button_height)
        
        draw_button(resume_button, ">> DEVAM ET", mouse_pos)
        draw_button(menu_button, "ANA MENÜ", mouse_pos)
        draw_button(quit_button, "X ÇIKIŞ", mouse_pos)
        
        draw_text("ESC - Devam Et", SMALL_FONT, LIGHT_GRAY, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        
        pygame.display.flip()
        clock.tick(60)
    
    return "quit"


def draw_credits_popup(mouse_pos):
    popup_width = 800
    popup_height = 650
    popup_rect = pygame.Rect(
        SCREEN_WIDTH // 2 - popup_width // 2,
        SCREEN_HEIGHT // 2 - popup_height // 2,
        popup_width, popup_height
    )

    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))

    pygame.draw.rect(screen, NAVY, popup_rect, border_radius=25)
    pygame.draw.rect(screen, CYAN, popup_rect, 5, border_radius=25)

    close_button_size = 40
    close_button_rect = pygame.Rect(
        popup_rect.right - close_button_size - 15,
        popup_rect.top + 15,
        close_button_size, close_button_size
    )

    close_hover = close_button_rect.collidepoint(mouse_pos)
    close_color = RED if close_hover else (150, 0, 0)

    pygame.draw.circle(screen, close_color, close_button_rect.center, close_button_size // 2)
    draw_text("X", SUBTITLE_FONT, WHITE, close_button_rect.centerx, close_button_rect.centery)

    center_x = popup_rect.centerx
    start_y = popup_rect.top + 70
    line_spacing = 40

    draw_text("HAZIRLAYANLAR", SUBTITLE_FONT, YELLOW, center_x, start_y)
    start_y += 80

    # GELİŞTİRİCİLER
    draw_text("Geliştirme", BUTTON_FONT, WHITE, center_x, start_y)
    draw_text("Emir Tevfik LAV", SMALL_FONT, LIGHT_GRAY, center_x, start_y + line_spacing)
    start_y += 50
    draw_text("Yusuf SÖĞÜT", SMALL_FONT, LIGHT_GRAY, center_x, start_y + line_spacing)
    start_y += 50
    draw_text("Emrullah KARADUMAN", SMALL_FONT, LIGHT_GRAY, center_x, start_y + line_spacing)
    start_y += 100

    # YAPAY ZEKA DESTEĞİ
    draw_text("Yapay Zeka Desteği", BUTTON_FONT, WHITE, center_x, start_y)
    draw_text("Kod Asistanı: Claude - Gemini", SMALL_FONT, LIGHT_GRAY, center_x, start_y + line_spacing)
    start_y += 50
    draw_text("Görsel Oluşturma Asistanı: Gemini", SMALL_FONT, LIGHT_GRAY, center_x, start_y + line_spacing)
    start_y += 100

    # OYUN KONUSU
    draw_text("Konu & Konsept", BUTTON_FONT, WHITE, center_x, start_y)
    draw_text("OSI Katmanları, Ağ Protokolleri, Ağ Cihazları", SMALL_FONT, LIGHT_GRAY, center_x, start_y + line_spacing)

    # Versiyon Bilgisi
    draw_text("Versiyon 1.0", SMALL_FONT, GRID_COLOR, center_x, popup_rect.bottom - 40)

    return close_button_rect

def show_level_intro(level_num, player_count=1, starting_player=1, start_reason=""):
    level_data = LEVELS[level_num]
    running = True
    
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    return "start"
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start_button.collidepoint(mouse_pos):
                    return "start"
                if back_button.collidepoint(mouse_pos):
                    return "menu"
        
        draw_gradient_background()
        
        draw_text(f"SEVİYE {level_num}", TITLE_FONT, YELLOW, SCREEN_WIDTH // 2, 200)
        draw_text(level_data["name"], SUBTITLE_FONT, CYAN, SCREEN_WIDTH // 2, 320)
        
        desc_box = pygame.Rect(SCREEN_WIDTH // 2 - 700, 400, 1400, 300)
        pygame.draw.rect(screen, (30, 40, 60), desc_box, border_radius=20)
        pygame.draw.rect(screen, PURPLE, desc_box, 4, border_radius=20)
        
        draw_text(level_data["description"], BUTTON_FONT, WHITE, SCREEN_WIDTH // 2, 510)
        draw_text(f"Toplam {len(level_data['pairs'])} eşleştirme yapacaksınız", SMALL_FONT, LIGHT_GRAY, SCREEN_WIDTH // 2, 600)

        if player_count == 2 and start_reason:
            info_box = pygame.Rect(SCREEN_WIDTH // 2 - 650, 630, 1300, 100)
            pygame.draw.rect(screen, (40, 50, 70), info_box, border_radius=15)
            
            player_color = PLAYER1_COLOR if starting_player == 1 else PLAYER2_COLOR
            pygame.draw.rect(screen, player_color, info_box, 3, border_radius=15)
            
            draw_text(start_reason, BUTTON_FONT, player_color, SCREEN_WIDTH // 2, info_box.centery)
        
        center_x = SCREEN_WIDTH // 2
        button_width = 450
        button_height = 90
        button_y = 760 if (player_count == 2 and start_reason) else 720
        
        start_button = pygame.Rect(center_x - button_width // 2, button_y, button_width, button_height)
        back_button = pygame.Rect(center_x - button_width // 2, button_y + 110, button_width, button_height)
        
        draw_button(start_button, ">> BAŞLA", mouse_pos)
        draw_button(back_button, "<< GERI", mouse_pos)
        
        draw_text("SPACE veya ENTER - Başla  |  ESC - Geri", SMALL_FONT, GRID_COLOR, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        
        pygame.display.flip()
        clock.tick(60)
    
    return "quit"


def play_level(level_num, player_scores, player_count=1, starting_player=1):
    level_data = LEVELS[level_num]
    pairs = level_data["pairs"]
    images = level_data.get("images", {})

    if level_num == 3:
        card_width = 140
        card_height = 187
        card_spacing = 20
        start_y = 200
        COLUMNS_PER_SIDE = 3
        EDGE_PADDING = 30
    else:
        card_width = 140
        card_height = 187
        card_spacing = 20
        start_y = 200
        COLUMNS_PER_SIDE = 2
        EDGE_PADDING = 30

    left_items = list(pairs.keys())
    left_cards = []
    left_x = EDGE_PADDING

    for i, key in enumerate(left_items):
        row = i // COLUMNS_PER_SIDE
        col = i % COLUMNS_PER_SIDE
        x = left_x + col * (card_width + card_spacing)
        y = start_y + row * (card_height + card_spacing)
        image_path = images.get(key, None)
        new_card = GameCard(key, x, y, card_width, card_height, key, image_path)
        left_cards.append(new_card)

    if level_num == 3:
        right_items = list(set(pairs.values()))
        right_items.sort()
    else:
        right_items = list(pairs.values())
        random.shuffle(right_items)

    right_cards = []

    SIDE_BLOCK_WIDTH = (COLUMNS_PER_SIDE * card_width) + ((COLUMNS_PER_SIDE - 1) * card_spacing)
    right_x_start = SCREEN_WIDTH - SIDE_BLOCK_WIDTH - EDGE_PADDING

    for i, value in enumerate(right_items):
        row = i // COLUMNS_PER_SIDE
        col = i % COLUMNS_PER_SIDE
        x = right_x_start + col * (card_width + card_spacing)
        y = start_y + row * (card_height + card_spacing)

        if level_num == 3:
            match_key = value
        else:
            match_key = [k for k, v in pairs.items() if v == value][0]

        image_path = images.get(value, None)
        new_card = GameCard(value, x, y, card_width, card_height, match_key, image_path)
        right_cards.append(new_card)

    current_player = starting_player
    player_matches = {1: 0, 2: 0}
    
    level_start_time = pygame.time.get_ticks()
    turn_timer = 5.0
    last_tick = pygame.time.get_ticks()
    paused_time = 0
    
    dragged_card = None
    notification = {"show": False, "text": "", "color": WHITE, "timer": 0}
    matches_made = 0
    total_pairs = len(pairs)
    
    running = True
    
    while running:
        mouse_pos = pygame.mouse.get_pos()
        current_time = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit", player_scores
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_start = pygame.time.get_ticks()
                    pause_result = show_pause_menu()
                    pause_end = pygame.time.get_ticks()
                    paused_time += (pause_end - pause_start)
                    
                    if pause_result == "quit":
                        return "quit", player_scores
                    elif pause_result == "menu":
                        return "menu", player_scores
                    last_tick = pygame.time.get_ticks()
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not dragged_card and not notification["show"]:
                    for c in left_cards:
                        if c.start_drag(mouse_pos):
                            dragged_card = c
                            break
                    
                    if not dragged_card:
                        for c in right_cards:
                            if c.start_drag(mouse_pos):
                                dragged_card = c
                                break
            
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if dragged_card and not notification["show"]:
                    check_match = None
                    
                    if dragged_card in left_cards:
                        for c in right_cards:
                            if c.rect.colliderect(dragged_card.rect) and not c.matched:
                                check_match = c
                                break
                    else:
                        for c in left_cards:
                            if c.rect.colliderect(dragged_card.rect) and not c.matched:
                                check_match = c
                                break

                    if check_match:
                        is_match = False
                        if level_num == 3:
                            if pairs.get(dragged_card.text) == check_match.text or pairs.get(
                                    check_match.text) == dragged_card.text:
                                is_match = True
                        else:
                            if dragged_card.match_key == check_match.match_key:
                                is_match = True

                        if is_match:
                            player_scores[current_player] += 10
                            dragged_card.matched = True
                            dragged_card.matched_by = current_player

                            if level_num != 3:
                                check_match.matched = True
                                check_match.matched_by = current_player

                            matches_made += 1
                            
                            if player_count == 1:
                                notif_text = "+10 PUAN! Doğru Eşleştirme!"
                            else:
                                notif_text = f"OYUNCU {current_player}: +10 PUAN! Doğru Eşleştirme!"
                            
                            notification = {
                                "show": True,
                                "text": notif_text,
                                "color": PLAYER1_COLOR if current_player == 1 else PLAYER2_COLOR,
                                "timer": 90
                            }
                            
                            turn_timer = 5.0
                        else:
                            player_scores[current_player] = max(0, player_scores[current_player] - 5)
                            
                            if player_count == 1:
                                notif_text = "-5 PUAN! Yanlış Eşleştirme!"
                            else:
                                notif_text = f"OYUNCU {current_player}: -5 PUAN! Sıra Değişti!"
                            
                            notification = {
                                "show": True,
                                "text": notif_text,
                                "color": RED,
                                "timer": 90
                            }
                            
                            turn_timer = 5.0
                            
                            if player_count == 2:
                                current_player = 2 if current_player == 1 else 1
                    
                    dragged_card.snap_back()
                    dragged_card.stop_drag()
                    dragged_card = None
            
            if event.type == pygame.MOUSEMOTION:
                if dragged_card and not notification["show"]:
                    dragged_card.drag(mouse_pos)
                elif dragged_card and notification["show"]:
                    dragged_card.snap_back()
                    dragged_card.stop_drag()
                    dragged_card = None
        
        if not notification["show"] and matches_made < total_pairs:
            delta = (current_time - last_tick) / 1000.0
            turn_timer -= delta
            
            if turn_timer <= 0:
                player_scores[current_player] = max(0, player_scores[current_player] - 5)
                
                if player_count == 1:
                    notif_text = "-5 PUAN! Süre Doldu!"
                else:
                    notif_text = f"OYUNCU {current_player}: Süre Doldu! Sira Değişti!"
                
                notification = {
                    "show": True,
                    "text": notif_text,
                    "color": RED,
                    "timer": 90
                }
                turn_timer = 5.0
                
                if player_count == 2:
                    current_player = 2 if current_player == 1 else 1
                
                if dragged_card:
                    dragged_card.snap_back()
                    dragged_card.stop_drag()
                    dragged_card = None
        
        last_tick = current_time
        
        if notification["show"]:
            notification["timer"] -= 1
            if notification["timer"] <= 0:
                notification["show"] = False
        
        if not notification["show"]:
            for c in left_cards + right_cards:
                c.update_hover(mouse_pos)
        else:
            for c in left_cards + right_cards:
                c.hover = False
        
        if matches_made == total_pairs:
            elapsed_time = (current_time - level_start_time - paused_time) / 1000.0
            result = show_level_complete(level_num, player_scores, elapsed_time, player_count, player_matches)
            return result, player_scores
        
        draw_gradient_background()
        
        panel_rect = pygame.Rect(50, 20, SCREEN_WIDTH - 100, 140)
        pygame.draw.rect(screen, (20, 30, 50), panel_rect, border_radius=15)
        pygame.draw.rect(screen, PURPLE, panel_rect, 3, border_radius=15)
        
        draw_text(level_data["name"], SUBTITLE_FONT, CYAN, SCREEN_WIDTH // 2, 50)
        
        if player_count == 1:
            draw_text(f"Puan: {player_scores[1]}", BUTTON_FONT, YELLOW, 200, 100)
            draw_text(f"Eşleştirme: {matches_made}/{total_pairs}", BUTTON_FONT, GREEN, SCREEN_WIDTH // 2, 100)
            
            timer_color = RED if turn_timer < 2 else (YELLOW if turn_timer < 4 else GREEN)
            draw_text(f"Süre: {turn_timer:.1f}s", BUTTON_FONT, timer_color, SCREEN_WIDTH - 200, 100)
        else:
            p1_alpha = 255 if current_player == 1 else 100
            p1_text = f"OYUNCU 1: {player_scores[1]}"
            p1_surf = BUTTON_FONT.render(p1_text, True, PLAYER1_COLOR)
            p1_surf.set_alpha(p1_alpha)
            p1_rect = p1_surf.get_rect(center=(250, 100))
            screen.blit(p1_surf, p1_rect)
            
            if current_player == 1:
                pygame.draw.circle(screen, PLAYER1_COLOR, (p1_rect.left - 30, p1_rect.centery), 12)
            
            timer_color = RED if turn_timer < 2 else (YELLOW if turn_timer < 4 else GREEN)
            draw_text(f"{turn_timer:.1f}s", BUTTON_FONT, timer_color, SCREEN_WIDTH // 2, 100)
            
            p2_alpha = 255 if current_player == 2 else 100
            p2_text = f"OYUNCU 2: {player_scores[2]}"
            p2_surf = BUTTON_FONT.render(p2_text, True, PLAYER2_COLOR)
            p2_surf.set_alpha(p2_alpha)
            p2_rect = p2_surf.get_rect(center=(SCREEN_WIDTH - 250, 100))
            screen.blit(p2_surf, p2_rect)
            
            if current_player == 2:
                pygame.draw.circle(screen, PLAYER2_COLOR, (p2_rect.right + 30, p2_rect.centery), 12)
            
            draw_text(f"Eşleştirme: {matches_made}/{total_pairs}", SMALL_FONT, WHITE, SCREEN_WIDTH // 2, 140)
        
        total_elapsed = (current_time - level_start_time - paused_time) / 1000.0
        draw_text(f"Toplam Süre: {int(total_elapsed)}s", SMALL_FONT, LIGHT_GRAY, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60)

        for c in left_cards:
            if c != dragged_card:
                c.draw(screen)

        for c in right_cards:
            if c != dragged_card:
                c.draw(screen)

        if dragged_card:
            dragged_card.draw(screen)
        
        if notification["show"]:
            notif_width = 850
            notif_height = 120
            notif_rect = pygame.Rect(SCREEN_WIDTH // 2 - notif_width // 2, 
                                     SCREEN_HEIGHT // 2 - notif_height // 2,
                                     notif_width, notif_height)
            
            pygame.draw.rect(screen, (0, 0, 0), notif_rect, border_radius=20)
            pygame.draw.rect(screen, notification["color"], notif_rect, 5, border_radius=20)
            draw_text(notification["text"], BUTTON_FONT, notification["color"], 
                     notif_rect.centerx, notif_rect.centery)
        
        draw_text("ESC - Duraklat", SMALL_FONT, GRID_COLOR, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30)
        
        pygame.display.flip()
        clock.tick(60)
    
    return "quit", player_scores

def show_level_complete(level_num, player_scores, time, player_count=1, player_matches=None):
    running = True
    
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if next_button.collidepoint(mouse_pos):
                    if level_num < 3:
                        return "next"
                    else:
                        return "complete"
                
                if menu_button.collidepoint(mouse_pos):
                    return "menu"
        
        draw_gradient_background()
        
        draw_text("SEVİYE TAMAMLANDI!", TITLE_FONT, GREEN, SCREEN_WIDTH // 2, 200)
        
        draw_text(f"Seviye {level_num}", SUBTITLE_FONT, CYAN, SCREEN_WIDTH // 2, 340)
        
        if player_count == 1:
            draw_text(f"Toplam Puan: {player_scores[1]}", SUBTITLE_FONT, YELLOW, SCREEN_WIDTH // 2, 420)
            draw_text(f"Süre: {int(time)} saniye", SUBTITLE_FONT, WHITE, SCREEN_WIDTH // 2, 490)
        else:
            draw_text(f"Oyuncu 1: {player_scores[1]} puan ({player_matches[1]} eşleştirme)",
                     SUBTITLE_FONT, PLAYER1_COLOR, SCREEN_WIDTH // 2, 420)
            draw_text(f"Oyuncu 2: {player_scores[2]} puan ({player_matches[2]} eşleştirme)",
                     SUBTITLE_FONT, PLAYER2_COLOR, SCREEN_WIDTH // 2, 490)
            
            if player_scores[1] > player_scores[2]:
                winner_text = "OYUNCU 1 KAZANDI!"
                winner_color = PLAYER1_COLOR
            elif player_scores[2] > player_scores[1]:
                winner_text = "OYUNCU 2 KAZANDI!"
                winner_color = PLAYER2_COLOR
            else:
                winner_text = "BERABERE!"
                winner_color = YELLOW
            
            draw_text(winner_text, SUBTITLE_FONT, winner_color, SCREEN_WIDTH // 2, 570)
            draw_text(f"Süre: {int(time)} saniye", SMALL_FONT, LIGHT_GRAY, SCREEN_WIDTH // 2, 640)
        
        center_x = SCREEN_WIDTH // 2
        button_width = 400
        button_height = 80
        
        if level_num < 3:
            next_button = pygame.Rect(center_x - button_width // 2, 720, button_width, button_height)
            menu_button = pygame.Rect(center_x - button_width // 2, 820, button_width, button_height)
            
            draw_button(next_button, ">> SONRAKİ SEVİYE", mouse_pos)
            draw_button(menu_button, "ANA MENÜ", mouse_pos)
        else:
            menu_button = pygame.Rect(center_x - button_width // 2, 720, button_width, button_height)
            next_button = menu_button
            
            draw_button(menu_button, "ANA MENÜ", mouse_pos)
        
        pygame.display.flip()
        clock.tick(60)
    
    return "quit"

def show_game_complete(player_scores, player_count=1):
    running = True
    
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if menu_button.collidepoint(mouse_pos):
                    return "menu"
        
        draw_gradient_background()
        
        draw_text("OYUN TAMAMLANDI!", TITLE_FONT, YELLOW, SCREEN_WIDTH // 2, 250)
        
        if player_count == 1:
            draw_text(f"Final Puan: {player_scores[1]}", SUBTITLE_FONT, GREEN, SCREEN_WIDTH // 2, 400)
        else:
            draw_text(f"Oyuncu 1: {player_scores[1]} puan", SUBTITLE_FONT, PLAYER1_COLOR, SCREEN_WIDTH // 2, 400)
            draw_text(f"Oyuncu 2: {player_scores[2]} puan", SUBTITLE_FONT, PLAYER2_COLOR, SCREEN_WIDTH // 2, 470)
            
            if player_scores[1] > player_scores[2]:
                winner_text = "GENEL KAZANAN: OYUNCU 1!"
                winner_color = PLAYER1_COLOR
            elif player_scores[2] > player_scores[1]:
                winner_text = "GENEL KAZANAN: OYUNCU 2!"
                winner_color = PLAYER2_COLOR
            else:
                winner_text = "GENEL SONUÇ: BERABERE!"
                winner_color = YELLOW
            
            draw_text(winner_text, SUBTITLE_FONT, winner_color, SCREEN_WIDTH // 2, 560)
        
        draw_text("Tum Seviyeleri TamamladınIz!", BUTTON_FONT, WHITE, SCREEN_WIDTH // 2, 650)
        
        center_x = SCREEN_WIDTH // 2
        button_width = 400
        button_height = 80
        
        menu_button = pygame.Rect(center_x - button_width // 2, 750, button_width, button_height)
        draw_button(menu_button, "ANA MENÜ", mouse_pos)
        
        pygame.display.flip()
        clock.tick(60)
    
    return "quit"

def single_player_game():
    current_level = 1
    player_scores = {1: 0}
    
    while current_level <= 3:
        intro_result = show_level_intro(current_level, player_count=1, starting_player=1, start_reason="")
        
        if intro_result == "quit":
            return "quit"
        elif intro_result == "menu":
            return "menu"
        elif intro_result == "start":
            result, player_scores = play_level(current_level, player_scores, player_count=1, starting_player=1)
            
            if result == "quit":
                return "quit"
            elif result == "menu":
                return "menu"
            elif result == "next":
                current_level += 1
            elif result == "complete":
                break
    
    return show_game_complete(player_scores, player_count=1)

def two_player_game():
    current_level = 1
    player_scores = {1: 0, 2: 0}
    
    while current_level <= 3:
        if current_level == 1:
            starting_player = random.choice([1, 2])
            start_reason = f"OYUNCU {starting_player} BAŞLAYACAK (Rastgele)"
        else:
            score_diff = abs(player_scores[1] - player_scores[2])
            
            if score_diff >= 5:
                if player_scores[1] < player_scores[2]:
                    starting_player = 1
                    start_reason = f"OYUNCU 1 BAŞLAYACAK (Geriden Geliyor: -{score_diff} puan)"
                else:
                    starting_player = 2
                    start_reason = f"OYUNCU 2 BAŞLAYACAK (Geriden Geliyor: -{score_diff} puan)"
            else:
                starting_player = random.choice([1, 2])
                if score_diff == 0:
                    start_reason = f"OYUNCU {starting_player} BAŞLAYACAK (Berabere - Rastgele)"
                else:
                    start_reason = f"OYUNCU {starting_player} BAŞLAYACAK (Çok Yakın - Rastgele)"
        
        intro_result = show_level_intro(current_level, player_count=2, starting_player=starting_player, start_reason=start_reason)
        
        if intro_result == "quit":
            return "quit"
        elif intro_result == "menu":
            return "menu"
        elif intro_result == "start":
            result, player_scores = play_level(current_level, player_scores, player_count=2, starting_player=starting_player)
            
            if result == "quit":
                return "quit"
            elif result == "menu":
                return "menu"
            elif result == "next":
                current_level += 1
            elif result == "complete":
                break
    
    return show_game_complete(player_scores, player_count=2)

def game_screen(player_count):
    if player_count == 1:
        return single_player_game()
    else:
        return two_player_game()

def main():
    current_screen = "menu"
    player_count = 1
    
    while True:
        if current_screen == "menu":
            current_screen = main_menu()
        elif current_screen == "play":
            current_screen, player_count = game_mode_screen()
        elif current_screen == "game":
            current_screen = game_screen(player_count)
        elif current_screen == "quit":
            break
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()