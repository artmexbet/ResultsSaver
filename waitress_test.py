from waitress import serve
import main_2

serve(main_2.app, host='0.0.0.0', port=8080)
