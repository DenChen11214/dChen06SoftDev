#Living Tribunal: Dennis Chen, Ricky Lin
#SoftDev pd6
#K10: Jinja Tuning ...
#2018-09-24

from flask import Flask, render_template
from util import occChoose
app = Flask(__name__)

@app.route("/")
def occupations():
    occDict, links = occChoose.dictFile("data/occupations.csv")
    occChosen, index = occChoose.occChooser()
    i = 0
    for key in occDict:
        occDict[key] = [occDict[key],links[i]] # makes dictionary include links w/ the percentage
        i += 1
    return render_template('LivingTribunal_chenD-linR.html',
                            random = occChosen,
                            link = links[index],
                            _dict = occDict)

if __name__ == '__main__':
    app.run(debug=True)
