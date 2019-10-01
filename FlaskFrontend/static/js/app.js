function initAdders() {
    const elAdd = document.querySelector('.list-add');
    if (elAdd) {
        elAdd.addEventListener('click', () => {
            const elVisible = document.querySelector('.list-add>div:not(.hidden)');
            const elHidden = elAdd.querySelector('.list-add>div.hidden');
            elVisible.classList.add('hidden');
            elHidden.classList.remove('hidden');
        });

        elAdd.querySelectorAll('.to-add').forEach((element) => {
                element.addEventListener('click', (ev) => {
                    const apiPath = ev.target.parentElement.getAttribute('data-path');
                    const addId = ev.target.parentElement.getAttribute('data-add-id');

                    const req = new XMLHttpRequest();
                    req.addEventListener('load', () => {
                        if (req.status === 200) location.reload();
                        else alert(`Error ${req.statusText}`);

                    });
                    req.addEventListener('error', (err) => alert(`Error: ${err}`));
                    req.open("POST", apiPath);
                    req.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
                    req.send(JSON.stringify({id: addId}));
                });
            }
        );
    }

}

function initBlockLinks() {
    document.querySelectorAll('.block-list-item').forEach((element) => {
        const href = element.getAttribute('data-href');
        if (href) element.addEventListener('click', () => {
            window.location.href = href
        });
    });
}

function init() {
    initAdders();
    initBlockLinks();
}

init();
