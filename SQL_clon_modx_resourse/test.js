function countWords() {
  chrome.tabs.executeScript({
    code: `
      const text = document.getElementsByTagName("body")[0].innerText;
      const title = document.getElementsByTagName("title")[0].innerText;
      const h1 = document.getElementsByTagName("h1")[0]?.innerText || '';
      const shozhi = text.toLowerCase().split(/[ ,.]+/).filter(word => title.toLowerCase().includes(word) || h1.toLowerCase().includes(word));
	    const metaDescription = document.querySelector('meta[name="description"]')?.content || '';

      // фільтруємо слова з "text", які часто зустрічаються
      const shozhiText = text.toLowerCase().split(/[ ,.]+/).filter(word => word.length > 2);

      // фільтруємо слова з "text", які зустрічаються в "title"
      const shozhiTitle = text.toLowerCase().split(/[ ,.]+/).filter(word => title.toLowerCase().includes(word));

      [text, title, h1, shozhi, metaDescription, shozhiText, shozhiTitle];
    `,
  }, function(result) {
    const [text, title, h1, shozhi, metaDescription, shozhiText, shozhiTitle] = result[0];
    const wordCount = text.trim().split(/\s+/).length;
    const charCount = text.length;

    // знаходження слів з кількістю входжень в тексті
    const wordOccurencesMap = {};
    shozhiText.forEach(word => {
      if (word.length > 3) {
        if (wordOccurencesMap.hasOwnProperty(word)) {
          wordOccurencesMap[word]++;
        } else {
          wordOccurencesMap[word] = 1;
        }
      }
    });
    const wordOccurences = Object.entries(wordOccurencesMap).sort((a, b) => b[1] - a[1]).slice(0, 10).map(([word, count]) => `${word} (<span class="red">${count}</span>)`).join(', ');

	// знаходження слів з "Description" які часто зустрічаються в "title"
    const metaDes = metaDescription.split(' ').map(word => {
      if (title.toLowerCase().includes(word.toLowerCase())) {
        return `<span class="red">${word}</span>`;
      } else {
        return word;
      }
    }).join(' ');

    // знаходження слів title з кількістю входжень в text
    const wordOccurencesMapTitle = {};
    shozhiTitle.forEach(word => {
      if (word.length > 2) {
        if (wordOccurencesMapTitle.hasOwnProperty(word)) {
          wordOccurencesMapTitle[word]++;
        } else {
          wordOccurencesMapTitle[word] = 1;
        }
      }
    });
    const wordOccurencesTitle = Object.entries(wordOccurencesMapTitle).sort((a, b) => b[1] - a[1]).slice(0, 10).map(([word, count]) => `${word} (<span class="red">${count}</span>)`).join(', ');

    const highlightedText = text.trim().split(/\s+/).map(word => {
      if (shozhi.includes(word.toLowerCase()) && word.length > 2) {
        return `<span class="myword">${word}</span>`;
      } else {
        return word;
      }
    }).join(" ");

    // знайти в "h1" слова що зустрічаються в "title", та огорнути тегом "span"
    const h1Words = h1.split(' ').map(word => {
      if (title.toLowerCase().includes(word.toLowerCase())) {
        return `<span class="red">${word}</span>`;
      } else {
        return word;
      }
    }).join(' ');

    document.getElementById('text').innerHTML = highlightedText;
    document.getElementById('wordCount').textContent = `${wordCount}`;
    document.getElementById('charCount').textContent = `${charCount}`;
    document.getElementById('title').textContent = `${title}`;
    document.getElementById('h1').innerHTML = h1Words;
    document.getElementById('metaDescription').innerHTML = metaDes;
    document.getElementById('wordOccurences').innerHTML = wordOccurences; // виведення з кількістю входжень в текстіь
    document.getElementById('wordOccurencesTitle').innerHTML = wordOccurencesTitle; // виведення слів title з кількістю входжень в text
  });
}

document.addEventListener('DOMContentLoaded', function() {
  countWords();
});
