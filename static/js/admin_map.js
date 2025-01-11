document.addEventListener("DOMContentLoaded", function () {
    // تعیین نقشه و مرکز اولیه
    const mapContainer = document.createElement("div");
    mapContainer.id = "map";
    mapContainer.style.height = "400px";
    mapContainer.style.marginTop = "20px";

    // افزودن نقشه به فرم
    const form = document.querySelector("fieldset"); // جایی که می‌خواهید نقشه اضافه شود
    form.appendChild(mapContainer);

    const map = new L.Map("map", {
        center: [35.7, 55.3],
        zoom: 13,
    });

    // افزودن لایه OpenStreetMap به نقشه
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: "© OpenStreetMap contributors",
    }).addTo(map);

    let marker;

    // یافتن فیلدهای latitude و longitude
    const latField = document.getElementById("id_latitude");
    const lngField = document.getElementById("id_longitude");

    // اگر مختصات قبلاً وارد شده‌اند، آن‌ها را روی نقشه نمایش دهید
    if (latField.value && lngField.value) {
        const lat = parseFloat(latField.value);
        const lng = parseFloat(lngField.value);
        marker = L.marker([lat, lng]).addTo(map);
        map.setView([lat, lng], 13);
    }

    // رویداد کلیک روی نقشه برای به‌روزرسانی مختصات
    map.on("click", function (e) {
        const { lat, lng } = e.latlng;

        // مقداردهی به فیلدهای مختصات
        latField.value = lat;
        lngField.value = lng;

        // اگر مارکری وجود دارد، حذفش کنید
        if (marker) {
            map.removeLayer(marker);
        }

        // افزودن مارکر جدید به نقشه
        marker = L.marker([lat, lng]).addTo(map);
    });
});
