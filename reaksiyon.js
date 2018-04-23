client.on('message', async msg => {
  if (msg.content.toLowerCase() === 'mesaj') { 
    await msg.react('-emoji- '); 
  }
  });