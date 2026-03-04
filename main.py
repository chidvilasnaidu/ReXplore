from flask import Flask, request, render_template
import re

app = Flask(__name__)

# ── Route 1: same as your @route('/') → renders ReXplore.html ──
@app.route('/')
def index():
    return render_template('ReXplore.html')

# ── Route 2: same as your @route('/Submit') → processes & renders result ──
@app.route('/execute', methods=['POST'])
def execute():
    pattern   = request.form.get('pattern', '').strip()
    test_str  = request.form.get('test_str', '')
    operation = request.form.get('operation', 'findall')
    replace   = request.form.get('replace', '')

    results = []
    output  = None
    error   = None

    if not pattern:
        error = "Please enter a regular expression pattern."
    elif not test_str and operation != 'compile':
        error = "Please enter a test string."
    else:
        try:
            if operation == 'findall':
                ms = re.findall(pattern, test_str)
                for i, m in enumerate(ms):
                    results.append({
                        'num': i+1, 'value': str(m),
                        'start': None, 'end': None,
                        'groups': list(m) if isinstance(m, tuple) else []
                    })

            elif operation == 'search':
                m = re.search(pattern, test_str)
                if m:
                    results.append({'num':1,'value':m.group(0),
                        'start':m.start(),'end':m.end(),'groups':list(m.groups())})

            elif operation == 'match':
                m = re.match(pattern, test_str)
                if m:
                    results.append({'num':1,'value':m.group(0),
                        'start':m.start(),'end':m.end(),'groups':list(m.groups())})

            elif operation == 'finditer':
                for i, m in enumerate(re.finditer(pattern, test_str)):
                    results.append({'num':i+1,'value':m.group(0),
                        'start':m.start(),'end':m.end(),'groups':list(m.groups())})

            elif operation == 'sub':
                output = re.sub(pattern, replace, test_str)

            elif operation == 'split':
                output = re.split(pattern, test_str)

            elif operation == 'compile':
                rx = re.compile(pattern)
                output = {'pattern': rx.pattern, 'flags': rx.flags, 'groups': rx.groups}

        except re.error as e:
            error = str(e)

    # Same as your render_template('result.html', name=name, age=age)
    return render_template('result.html',
        pattern=pattern, test_str=test_str,
        operation=operation, replace=replace,
        results=results, output=output, error=error)

if __name__ == '__main__':
    app.run(debug=True)