  onclick = "confirmDelete('{{row[1]}}')" 

  function confirmDelete(message) {
    console.log(message)
    const ask = "確定要刪除留言?【" + message + "】";
    const yes = confirm(ask);
    if (!yes) {
      window.event.returnValue = false;
    }
  }