// Função para alternar a visibilidade de uma div oculta ao clicar em um elemento
function toggleDiv(element, targetId) {
    // Encontra o elemento alvo pelo ID
    const targetElement = document.getElementById(targetId);
    
    if (!targetElement) {
        console.error('Elemento não encontrado com ID:', targetId);
        return;
    }
    
    // Verifica o estado atual
    const isHidden = window.getComputedStyle(targetElement).display === 'none';
    
    // Alterna entre mostrar e ocultar
    if (isHidden) {
        targetElement.style.display = 'block';
    } else {
        targetElement.style.display = 'none';
    }
}

// Versão com toggle de classe (melhor prática para animações CSS)
function toggleDivClass(element, targetSelector) {
    const targetElement = document.querySelector(targetSelector);
    
    if (!targetElement) {
        console.error('Elemento não encontrado com selector:', targetSelector);
        return;
    }
    
    // Alterna a classe 'aberto' ou 'fechado'
    targetElement.classList.toggle('aberto');
}

// Versão para acordeão (um por vez - fecha outros ao abrir)
function toggleAccordion(element, targetClass) {
    const container = element.closest('.matches-row')?.querySelector(targetClass);
    
    if (!container) {
        console.error('Container do acordeão não encontrado');
        return;
    }
    
    // Fecha todos os outros accordions primeiro (modo "um por vez")
    document.querySelectorAll('.matches-row.aberto').forEach(row => {
        const container = row.querySelector(targetClass);
        if (container) {
            container.style.display = 'none';
            row.classList.remove('aberto');
        }
    });
    
    // Abre o atual
    container.style.display = 'flex';
    element.classList.add('aberto');
}

// Função para adicionar/remover classe de matches-row ao clicar
function toggleMatchesRow(element) {
    // Adiciona/Remove a classe matches-row-open
    const matchesRow = element.closest('.matches-row');
    
    if (matchesRow) {
        matchesRow.classList.toggle('matches-row-open');
    } else {
        console.error('Elemento não encontrado dentro de .matches-row');
    }
}
