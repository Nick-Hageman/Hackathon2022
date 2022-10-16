function handleSubmit () {
    const name = document.getElementById('search').value;
    /*localStorage.setItem("SEARCH", name);
    */

    sessionStorage.setItem("SEARCH", search);
    return;
    }