## Воспроизводимость

Окружение:

* Python >= 3.10
* зависимости указаны в requirements.txt

Установка:

* pip install -r requirements.txt
* pip install -e .

Запуск:

* python scripts/run_experiment.py --config configs/base.yaml
* python scripts/make_plots.py --input results/raw --output reports/figures

Результаты:

* results/raw: CSV с метриками прогонов
* reports/figures: графики

Данные:

* изображения не хранятся в git
* см. data/README.md
