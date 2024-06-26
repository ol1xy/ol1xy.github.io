let slideIndex = 0;
        let slides = document.getElementsByClassName("slide");
        let dots = document.getElementsByClassName("dot");

        function showSlides() {
            for (let i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";
                dots[i].className = dots[i].className.replace(" active", "");
            }
            slides[slideIndex].style.display = "block";
            dots[slideIndex].className += " active";
        }

        function currentSlide(index) {
            slideIndex = index;
            showSlides();
        }

        function plusSlides(n) {
            slideIndex += n;
            if (slideIndex >= slides.length) {
                slideIndex = 0;
            } else if (slideIndex < 0) {
                slideIndex = slides.length - 1;
            }
            showSlides();
        }

        document.addEventListener("DOMContentLoaded", function() {
            const prevButton = document.querySelector(".prev");
            const nextButton = document.querySelector(".next");

            prevButton.addEventListener("click", () => {
                plusSlides(-1);
            });

            nextButton.addEventListener("click", () => {
                plusSlides(1);
            });

            showSlides();
        });

        // Добавление функции для перетаскивания слайдера
        const slider = document.querySelector('.slides');
        let isDragging = false;
        let startPos = 0;
        let currentTranslate = 0;
        let prevTranslate = 0;
        let animationID = 0;
        let currentIndex = 0;

        slider.addEventListener('mousedown', (e) => {
          isDragging = true;
          startPos = e.clientX;
          animationID = requestAnimationFrame(animation);
        });

        slider.addEventListener('mouseup', () => {
          isDragging = false;
          cancelAnimationFrame(animationID);
          const movedBy = currentTranslate - prevTranslate;

          if (movedBy < -100 && currentIndex < slides.length - 1) {
            currentIndex += 1;
          }

          if (movedBy > 100 && currentIndex > 0) {
            currentIndex -= 1;
          }

          setPositionByIndex();
        });

        slider.addEventListener('mouseleave', () => {
          isDragging = false;
          cancelAnimationFrame(animationID);
          setPositionByIndex();
        });

        slider.addEventListener('mousemove', (e) => {
          if (isDragging) {
            const currentPosition = e.clientX;
            currentTranslate = prevTranslate + currentPosition - startPos;
          }
        });

        function animation() {
          setSliderPosition();
          if (isDragging) requestAnimationFrame(animation);
        }

        function setSliderPosition() {
          slider.style.transform = `translateX(${currentTranslate}px)`;
        }

        function setPositionByIndex() {
          currentTranslate = currentIndex * -window.innerWidth;
          prevTranslate = currentTranslate;
          setSliderPosition();
        }

        // Добавление функции для интерактивной картинки
        const interactiveImage = document.getElementById("interactive-image");
        let scale = 1;
        let rotation = 0;
        let isDraggingImage = false;
        let startX = 0;
        let startY = 0;
        let translateX = 0;
        let translateY = 0;

        interactiveImage.addEventListener('mousedown', (e) => {
            isDraggingImage = true;
            startX = e.clientX - translateX;
            startY = e.clientY - translateY;
            interactiveImage.style.cursor = 'grabbing';
        });

        window.addEventListener('mouseup', () => {
            isDraggingImage = false;
            interactiveImage.style.cursor = 'grab';
        });

        window.addEventListener('mousemove', (e) => {
            if (isDraggingImage) {
                translateX = e.clientX - startX;
                translateY = e.clientY - startY;
                interactiveImage.style.transform = `translate(${translateX}px, ${translateY}px) scale(${scale}) rotate(${rotation}deg)`;
            }
        });

        window.addEventListener('wheel', (e) => {
            if (slides[slideIndex].contains(interactiveImage)) {
                if (e.deltaY > 0) {
                    scale *= 0.9;
                } else {
                    scale *= 1.1;
                }
                interactiveImage.style.transform = `translate(${translateX}px, ${translateY}px) scale(${scale}) rotate(${rotation}deg)`;
            }
        });

        interactiveImage.addEventListener('dblclick', () => {
            rotation = (rotation + 90) % 360;
            interactiveImage.style.transform = `translate(${translateX}px, ${translateY}px) scale(${scale}) rotate(${rotation}deg)`;
        });