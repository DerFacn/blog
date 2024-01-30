# 🥝Kiwi blog

Welcome to the 🥝Kiwi blog project! This is a monolithic Flask-based blog system.

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/derfacn/blog.git
   ```

2. Create a virtual environment in the project directory:

   ```bash
   cd blog
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Customize configurations:

   - In `config.py` update the configurations according to your needs.

   - Alternatively, you can create a `.env` file in the project root and set the configurations there.

6. Start the application using Gunicorn:

   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
   ```

   Replace `4` with the desired number of workers, and `5000` with the desired port.

### Usage

- Open your web browser and navigate to `http://127.0.0.1:5000` (or the port you specified) to access the blog application.

### Contributing

Feel free to contribute to this project by submitting bug reports, feature requests, or pull requests. Please follow the contribution guidelines.

### License
<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/derfacn/blog">🥝Kiwi blog</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/derfacn">Nikita Lupalo</a> is licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>