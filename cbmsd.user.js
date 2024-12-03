// ==UserScript==
// @name         Osu!CBMSD Tampermonkey
// @namespace    http://privatekey.is-a.dev
// @version      0.3
// @description  Modify osu! elements only if the local server is available and URL matches criteria.
// @author       PrivateKey
// @match        https://osu.ppy.sh/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    const checkServerStatus = async () => {
        try {
            const response = await fetch('http://localhost:8081/api/status');
            if (response.status === 200) {
                console.log("Local server is active. Monitoring URL...");
                monitorUrlChanges();
            } else {
                console.warn("Local server is not active. Changes will not be applied.");
            }
        } catch (error) {
            console.error("Failed to connect to local server:", error);
        }
    };

    const applyChanges = () => {
        const match = window.location.pathname.match(/^\/beatmapsets\/(\d+)/);
        const beatmapsetId = match ? match[1] : null;

        if (beatmapsetId) {
            // Change links
            const originalLink = document.querySelector(`a[href*="https://osu.ppy.sh/home/support"]`);
            if (originalLink) {
                originalLink.href = `http://localhost:8081/d/${beatmapsetId}`;
            }

            // Update "osu!direct" span and add new span inside
            const spanElements = document.querySelectorAll('span');
            spanElements.forEach(span => {
                if (span.textContent.includes("osu!direct")) {
                    span.textContent = "osu!cbmsd";

                    if (!span.querySelector('.btn-osu-big__icon')) { // Avoid duplicates
                        const newSpan = document.createElement('span');
                        newSpan.className = 'btn-osu-big__icon';
                        newSpan.innerHTML = '<span class="fa fa-fw"><span class="fas fa-download"></span></span>';
                        span.appendChild(newSpan);
                    }
                }
            });
        }
    };

    const monitorUrlChanges = () => {
        setInterval(() => {
            const match = window.location.pathname.match(/^\/beatmapsets\/(\d+)/);
            if (match) {
                applyChanges();
            }
        }, 500);
    };

    // Check server status before starting URL monitoring
    checkServerStatus();
})();
