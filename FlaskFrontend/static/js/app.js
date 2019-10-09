function get(url) {
    return new Promise((resolve, reject) => {
        var req = new XMLHttpRequest();
        req.open('GET', url);

        req.onload = (ev) => {
            if (req.status == 200) resolve(req.response); // Resolve with response if OK
            else reject(Error(req.statusText)); // Reject with statusText if not
        };
        req.onerror = () => reject(Error("Network Error"));
        req.send();
    });
}

function post(url, body) {
    return new Promise((resolve, reject) => {
        const req = new XMLHttpRequest();
        req.onload = (ev) => {
            if (req.status == 200 || req.status == 201) resolve(req.response); // Resolve with response if OK
            else reject(Error(req.statusText)); // Reject with statusText if not
        };
        req.onerror = () => reject(Error("Network Error"));
        req.open("POST", url);
        req.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        req.send(JSON.stringify(body));
    });

}

function toggle_child_visibility(elementSelector, parentElement) {
    const base = parentElement ? parentElement : document;
    const elVisible = base.querySelector(`${elementSelector}>div:not(.hidden)`);
    const elHidden = base.querySelector(`${elementSelector}>div.hidden`);
    if(elVisible) elVisible.classList.add('hidden');
    if(elHidden) elHidden.classList.remove('hidden');
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
    initBlockLinks();
}

init();
window.App = {};
window.App.req = {get, post};
window.App.util = {toggle_child_visibility};
