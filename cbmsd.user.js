// ==UserScript==
// @name         Osu!CBMSD Tampermonkey
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://osu.ppy.sh/beatmapsets/*
// @match        https://osu.ppy.sh/home/support
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    const match = window.location.pathname.match(/beatmapsets\/(\d+)/);
    const beatmapsetId = match ? match[1] : null;
    let linkChanged = 0;

    setInterval(() => {
        if (beatmapsetId && linkChanged < 5) {
            const originalLink = document.querySelector(`a[href*="https://osu.ppy.sh/home/support"]`);
            originalLink.href = `http://localhost:8081/d/${beatmapsetId}`;
            linkChanged += 1;
        }
    }, 2000);
})();

