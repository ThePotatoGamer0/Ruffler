import os

def generate_html_buttons(games_folder):
  """Generates HTML code for buttons to launch SWF games."""
  html = ""
  for game_folder in os.listdir(games_folder):
    game_path = os.path.join(games_folder, game_folder)
    if os.path.isdir(game_path):
      swf_file = os.path.join(game_path, 'game.swf')
      if os.path.isfile(swf_file):
        logo_file = os.path.join(game_path, 'logo.png')
        logo_url = logo_file.replace("\\", "/")  # Replace backslashes with forward slashes
        html_game_path = game_path.replace("\\", "/").replace("  ", "%20")
        html += f"""
          <button onclick="window.location.href='ruffle_player.html?game=./{html_game_path}/game.swf'" class="gamebutton">{game_folder}</button>
        """
  return html

if __name__ == "__main__":
  games_folder = "games"  # Replace with your actual games folder name
  html_code = generate_html_buttons(games_folder)
  print(html_code)
