#!/usr/bin/env python3
"""
Script para adicionar resultados ao projeto temporada-2029

Uso básico (1 resultado):
    python add_result.py "🟢 Corinthians 3 x 1 Palmeiras" --competicao brasileirao-serie-a

Uso batch (vários resultados de uma vez):
    python add_result.py "🟢 Corinthians 3 x 1 Palmeiras" \
        "🔴 Flamengo 2 x 1 Corinthians" \
        "⚪ Botafogo 1 x 1 Corinthians" \
        --competicao brasileirao-serie-a

Ou no modo batch (batch):
    python add_result.py --batch \
        --results "🟢 Corinthians 3 x 1 Palmeiras;🔴 Flamengo 2 x 1 Corinthians;⚪ Botafogo 1 x 1 Corinthians" \
        --competicao brasileirao-serie-a
"""

import re
import sys
import os

# Caminhos dos arquivos HTML
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_FILES = {
    'brasileirao-serie-a': (os.path.join(BASE_DIR, 'index.html'), '.\\brasileirao-serie-a\\'),
    'copa-libertadores-2029': (os.path.join(BASE_DIR, 'copa-libertadores-2029.html'), '.\\libertadores\\'),
    'copa-do-brasil': (os.path.join(BASE_DIR, 'copa-do-brasil.html'), '.\\brasileirao-serie-a\\'),
}

# Mapeamento de indicadores por resultado
def get_indicator_class(result):
    """Retorna a classe do indicador baseada no placar"""
    if result['home_score'] > result['away_score']:
        return 'indicator-victory'
    elif result['home_score'] < result['away_score']:
        return 'indicator-defeat'
    else:
        return 'indicator-draw'

def parse_result(result_string):
    """
    Parseia string de resultado simples
    Ex: "🟢 Corinthians 3 x 1 Palmeiras"
    
    Retorna dict com:
    {
        'home_team': 'Corinthians',
        'away_team': 'Palmeiras',
        'home_score': 3,
        'away_score': 1,
        'indicator_emoji': '🟢',
        'is_home_win': True,
        # ...
    }
    """
    # Regex para extrair: emoji + home_team + home_score x away_score + away_team
    pattern = r'([🟢⚪🔴])\s*(.+?)\s+(\d+)\s+x\s+(\d+)\s+(.+)'
    
    match = re.match(pattern, result_string.strip())
    if not match:
        raise ValueError(f"Formato inválido: {result_string}")
    
    emoji, home_team, home_score_str, away_score_str, away_team = match.groups()
    
    return {
        'indicator_emoji': emoji,
        'home_team': home_team.strip(),
        'away_team': away_team.strip(),
        'home_score': int(home_score_str),
        'away_score': int(away_score_str),
        'is_home_win': int(home_score_str) > int(away_score_str),
        'is_away_win': int(home_score_str) < int(away_score_str),
        'is_draw': int(home_score_str) == int(away_score_str),
    }

def get_image_path(team_name, team_folder):
    """Gera o caminho da imagem do logo baseada no nome do time"""
    return f"{team_folder}{team_name.lower().replace(' ', '-').replace('ã', 'a').replace('ó', 'o').replace('á', 'a').replace('é', 'e').replace('ú', 'u').replace('ü', 'u').replace('à', 'a')}-logo-footylogos-320.webp"

def get_indicator_emoji_value(result):
    emoji = result['indicator_emoji']
    if emoji == '🟢':
        return '🟢'
    elif emoji == '🔴':
        return '🔴'
    else:
        return '⚪'

# Mapeamento de Emojis para Classes HTML
# 🟢 = vitória, ⚪ = empate, 🔴 = derrota
EMOJI_TO_CLASS_MAP = {
    '🟢': 'indicator-victory',  # Vitória do time da casa
    '⚪': 'indicator-draw',      # Empate
    '🔴': 'indicator-defeat',   # Derrota do time da casa (vitória visitante)
}

def get_indicator_class_from_emoji(emoji):
    """Converte emoji do resultado para a classe HTML correspondente.
    
    Args:
        emoji: O emoji do resultado ('🟢', '⚪' ou '🔴')
    
    Returns:
        A classe HTML correspondente ('indicator-victory', 'indicator-draw', ou 'indicator-defeat')
    
    Exemplo:
        >>> get_indicator_class_from_emoji('🟢')
        'indicator-victory'
        >>> get_indicator_class_from_emoji('⚪')
        'indicator-draw'
        >>> get_indicator_class_from_emoji('🔴')
        'indicator-defeat'
    """
    return EMOJI_TO_CLASS_MAP.get(emoji, 'indicator-draw')  # Padrão: empate se emoji desconhecido

def add_result_to_html(html_content, team_folder, parse_result_data):
    """
    Adiciona novo resultado ao final da lista de jogos no HTML
    
    Args:
        html_content: Conteúdo atual do HTML
        team_folder: Pasta onde estão os logos (para gerar paths corretos)
        parse_result_data: Dados do resultado parseado
        
    Returns:
        Novo conteúdo HTML com o jogo adicionado
    """
    # Mapeamento de qual logo usar baseado na competição
    logo_folder_mapping = {
        'brasileirao-serie-a': '.\\brasileirao-serie-a\\',
        'copa-libertadores-2029': '.\\libertadores\\',
        'copa-do-brasil': '.\\brasileirao-serie-a\\',  # Usa mesmo folder do brasileirao por enquanto
    }
    
    # Determinar qual logo usar (prioriza o time da casa, mas pode vir do outro folder)
    team_folder = logo_folder_mapping.get(team_folder, team_folder)
    
    home_team_clean = parse_result_data['home_team']
    away_team_clean = parse_result_data['away_team']
    home_score = parse_result_data['home_score']
    away_score = parse_result_data['away_score']
    indicator_class = get_indicator_class_from_emoji(parse_result_data['indicator_emoji'])
    
    # Gerar paths das imagens
    home_image_path = get_image_path(home_team_clean, team_folder)
    away_image_path = get_image_path(away_team_clean, team_folder)
    
    # Criar HTML do novo jogo
    new_game_html = f'''

            <!-- Novo Jogo -->
            <div class="matches-row">
                <div class="{indicator_class}"></div>
                <div class="row">
                    <div class="time-casa">
                        <div class="nome-do-time-casa">{home_team_clean}</div>
                        <div class="img-wrapper"><img src="{home_image_path}" alt="{home_team_clean}"></div>
                    </div>

                    <div class="placar">
                        <div class="ponto-casa">{home_score}</div>
                        <div class="versus">X</div>
                        <div class="ponto-visitante">{away_score}</div>
                    </div>

                    <div class="time-visitante">
                        <div class="img-wrapper"><img src="{away_image_path}" alt="{away_team_clean}"></div>
                        <div class="nome-do-time-fora">{away_team_clean}</div>
                    </div>
                </div>
            </div>'''
    
    # Adicionar o novo jogo APENAS no final (antes da tag </body>)
    # Isso evita substituir conteúdo existente em chamadas múltiplas
    last_match = re.search(r'</div>\s*\n</body>', html_content, re.DOTALL)
    
    if last_match:
        # Adicionar logo antes do fechamento do body
        insert_pos = last_match.start()
        before_last_row = html_content[:insert_pos]
        after_last_row = html_content[insert_pos:]
        return before_last_row + new_game_html + '\n' + after_last_row
    else:
        # Não encontrou posição válida, apenas concatena no final (fallback)
        return html_content + new_game_html

def parse_batch_results(results_string):
    """
    Parseia string de múltiplos resultados separados por ponto e vírgula
    
    Ex: "🟢 Corinthians 3 x 1 Palmeiras;🔴 Flamengo 2 x 1 Corinthians"
    
    Retorna lista de dicts parseados
    """
    individual_results = results_string.strip().split(';')
    parsed_results = []
    
    for result in individual_results:
        if result.strip():
            try:
                parsed_results.append(parse_result(result))
            except ValueError as e:
                print(f"⚠️  Erro ao parsear: {result}")
                print(f"   {e}")
    
    return parsed_results

def main():
    """Main function"""
    # Verificar modo batch
    is_batch_mode = '--batch' in sys.argv
    
    if not is_batch_mode and len(sys.argv) < 2:
        print("Uso básico (1 resultado):")
        print('  python add_result.py "🟢 Corinthians 3 x 1 Palmeiras" --competicao [brasileirao-serie-a|copa-libertadores-2029|copa-do-brasil]')
        print()
        print("Uso batch (vários resultados):")
        print('  python add_result.py "🟢 A;🔴 B;⚪ C" --batch --competicao [brasileirao-serie-a|copa-libertadores-2029|copa-do-brasil]')
        sys.exit(1)
    
    competicao = None
    
    # Identificar modo de execução
    if is_batch_mode:
        # Modo batch
        if '--results' not in sys.argv or len(sys.argv) < 3:
            print("Erro: Modo batch requer --results com os resultados")
            sys.exit(1)
        
        results_string = sys.argv[sys.argv.index('--results') + 1]
        competicao_arg_idx = sys.argv.index('--competicao')
        competicao = sys.argv[competicao_arg_idx + 1].lower() if competicao_arg_idx + 1 < len(sys.argv) else None
        
    else:
        # Modo individual (um por vez ou múltiplos em linha)
        result_strings = []
        
        # Processar argumentos até encontrar --competicao
        for i, arg in enumerate(sys.argv):
            if arg == '--competicao':
                break
            
            # Verifica se este argumento é um resultado (começa com emoji e tem x)
            if any(emoji in arg for emoji in ['🟢', '⚪', '🔴']) and 'x' in arg:
                result_strings.append(arg)
        
        # Se não houver resultados, verificar se é comando de ajuda
        if not result_strings:
            print("Uso básico (1 resultado):")
            print('  python add_result.py "🟢 Corinthians 3 x 1 Palmeiras" --competicao [brasileirao-serie-a|copa-libertadores-2029|copa-do-brasil]')
            print()
            print("Uso batch (vários resultados de uma vez):")
            print('  python add_result.py "🟢 A;🔴 B;⚪ C" --batch --competicao [brasileirao-serie-a|copa-libertadores-2029|copa-do-brasil]')
            sys.exit(1)
        
        # Verificar se há --competicao
        competicao_arg_idx = sys.argv.index('--competicao') if '--competicao' in sys.argv else -1
        
        if competicao_arg_idx >= 0 and competicao_arg_idx + 1 < len(sys.argv):
            competicao = sys.argv[competicao_arg_idx + 1].lower()
    
    if not competicao:
        print("Erro: Você precisa especificar a competição!")
        print("Uso: python add_result.py \"🟢 Corinthians 3 x 1 Palmeiras\" --competicao brasileirao-serie-a")
        sys.exit(1)
    
    if competicao not in HTML_FILES:
        print(f"Erro: Competição inválida. Escolha entre:")
        for c in HTML_FILES.keys():
            print(f"  - {c}")
        sys.exit(1)
    
    try:
        # Parsear resultados (pode ser 1 ou mais)
        if len(result_strings) == 0 and is_batch_mode:
            # Modo batch sem --results explícito
            results_string = ' '.join(sys.argv[2:])

            parsed_results = parse_batch_results(results_string)
        else:
            # Separar resultados múltiplos por ponto e vírgula dentro de cada string
            final_parsed_results = []
            for rs in result_strings:
                # Se a string contém semicolos, separa-os
                if ';' in rs:
                    individual_results = rs.strip().split(';')
                    for ind_result in individual_results:
                        if ind_result.strip():  # Ignora strings vazias
                            parsed = parse_result(ind_result)
                            final_parsed_results.append(parsed)
                else:
                    # Apenas um resultado na string
                    parsed = parse_result(rs)
                    final_parsed_results.append(parsed)
            parsed_results = final_parsed_results

        
        if not parsed_results:
            print("Nenhum resultado válido encontrado!")
            sys.exit(1)
        
        # Ler conteúdo atual do arquivo
        html_file_path, team_folder = HTML_FILES[competicao]
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Adicionar todos os resultados
        new_html_content = html_content
        
        for result_data in parsed_results:
            new_html_content = add_result_to_html(new_html_content, team_folder, result_data)
        
        # Escrever de volta no arquivo
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(new_html_content)
        
        print(f"✅ {len(parsed_results)} resultado(s) adicionado(s) com sucesso!")
        print(f"📄 Arquivo atualizado: {os.path.basename(html_file_path)}")
        print(f"{competicao}")
        print()
        
        # Exibir resultados adicionados
        print("Novos jogos:")
        for i, result_data in enumerate(parsed_results, start=1):
            emoji = result_data['indicator_emoji']
            home_name = result_data['home_team']
            away_name = result_data['away_team']
            home_score = result_data['home_score']
            away_score = result_data['away_score']
            print(f"   {i}. {emoji} {home_name} ({home_score}) ✈️  {away_name} ({away_score})")
        
    except ValueError as e:
        print(f"❌ Erro ao parsear resultado: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro não esperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()