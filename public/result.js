window.addEventListener('load', () => {
    /*const params = (new URL(document.location)).searchParams;
    const search = params.get('search');

    document.getElementById('search').innerHTML = search*/
    const search = sessionStorage.getItem('SEARCH');

    document.getElementById('result-search').innerHTML = search;
})