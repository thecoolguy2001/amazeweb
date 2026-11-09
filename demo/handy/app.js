/* Handy — opening-hours status. Edit HOURS to match the business.
   Keys are JS weekdays (0 = Sunday). [openHour, closeHour] in 24h, or null for closed. */
(() => {
  const el = document.getElementById('status');
  if (!el) return;

  const HOURS = {0:null, 1:[7,20], 2:[7,20], 3:[7,20], 4:[7,20], 5:[7,20], 6:[8,17]};
  const NAMES = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];

  const fmt = h => {
    const ampm = h >= 12 ? 'pm' : 'am';
    const n = h % 12 || 12;
    return n + ampm;
  };

  const now = new Date();
  const today = HOURS[now.getDay()];
  const hour = now.getHours() + now.getMinutes() / 60;

  if (today && hour >= today[0] && hour < today[1]) {
    el.textContent = `Open now, until ${fmt(today[1])}`;
  } else {
    let i = 1, next = null;
    while (i <= 7 && !next) {
      const d = (now.getDay() + i) % 7;
      if (HOURS[d]) next = {day: NAMES[d], open: HOURS[d][0]};
      i++;
    }
    const opensToday = today && hour < today[0];
    el.textContent = opensToday
      ? `Closed, opens at ${fmt(today[0])}`
      : `Closed, opens ${next.day} at ${fmt(next.open)}`;
  }
})();
