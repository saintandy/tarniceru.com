let windowWidth = window.innerWidth;
let styleElement = document.createElement('style');

function appendFilter() {
  styleElement.innerHTML = `
  #filter {
    height: 100%;
    width: 100%;
    background: linear-gradient(
      -135deg,
      rgba(255, 255, 255, 0.18) 25%,
      rgba(255, 255, 255, 0.7) calc(25% + 1px),
      rgba(255, 255, 255, 0.12) calc(25% + 1px),
      rgba(255, 255, 255, 0.12) calc(50%),
      rgba(255, 255, 255, 0.7) calc(50% + 1px),
      rgba(255, 255, 255, 0.06) calc(50% + 1px),
      rgba(255, 255, 255, 0.06) calc(75%),
      rgba(255, 255, 255, 0.7) calc(75% + 1px),
      rgba(255, 255, 255, 0.0) calc(75% + 1px),
      rgba(255, 255, 255, 0.06) calc(100%)
    )
  }
  `;
  document.head.appendChild(styleElement);
}

function removeFilter() {
  document.head.removeChild(styleElement);
}

function adaptWidthToFontSize() {
  if (windowWidth < 400) {
    document.body.style.fontSize = "8px";
  } else if (windowWidth < 500) {
    document.body.style.fontSize = "10px";
  } else if (windowWidth < 700) {
    document.body.style.fontSize = "12px";
  } else {
    document.body.style.fontSize = "16px";
  }
}

appendFilter();
adaptWidthToFontSize();
window.addEventListener('resize', () => {
  windowWidth = window.innerWidth;
  adaptWidthToFontSize();
});

document.body.style.display = 'none';
document.body.onload = () => {
  document.body.style.display = 'block';
};
