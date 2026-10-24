/**
 * Navegação - Estado dos botões de navegação
 * Adiciona/remove a classe 'pressed' nos botões da classe .navegador
 */

(function() {
    // Função principal para atualizar o estado
    function updateNavButtons() {
        const pathname = window.location.pathname;
        
        // Remove a classe 'pressed' de todos os botões da navegação
        document.querySelectorAll('.navegador button').forEach(function(btn) {
            btn.classList.remove('pressed');
        });
        
        // Adiciona a classe 'pressed' ao botão correspondente baseado no href do link
        const navegadores = document.querySelectorAll('.navegador');
        
        navegadores.forEach(function(navegador) {
            const botaoLinks = navegador.querySelectorAll('.botao[onclick]');
            
            botaoLinks.forEach(function(btn) {
                // Extrai o caminho do onclick
                const onclickAttr = btn.getAttribute('onclick');
                
                if (onclickAttr && (onclickAttr.includes('./roma.html') || onclickAttr.includes('roma.html'))) {
                    if (pathname.endsWith('/roma.html')) {
                        btn.classList.add('pressed');
                    }
                } else if (onclickAttr && (onclickAttr.includes('./japao.html') || onclickAttr.includes('japao.html'))) {
                    if (pathname.endsWith('/japao.html')) {
                        btn.classList.add('pressed');
                    }
                } else if (onclickAttr && (onclickAttr.includes('./brasil.html') || onclickAttr.includes('brasil.html'))) {
                    if (pathname.endsWith('/brasil.html')) {
                        btn.classList.add('pressed');
                    }
                }
            });
            
            // Identifica o botão "atual" (sem onclick para links externos)
            const currentBtn = navegador.querySelector('.botao:not([onclick])');
            if (currentBtn && pathname.endsWith('/home.html')) {
                currentBtn.classList.add('pressed');
            }
        });
    }
    
    // Executa ao carregar a página
    document.addEventListener('DOMContentLoaded', updateNavButtons);
    
})();