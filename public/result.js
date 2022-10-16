window.addEventListener('load', () => {
    const params = (new URL(document.location)).searchParams;
    const search = params.get('search');

    document.getElementById('search').innerHTML = search
})