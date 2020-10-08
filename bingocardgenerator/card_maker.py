# from Olivia Ng via https://codepen.io/oliviale/pen/OrxWyK

def write_card(
        card_title,
        card_subtitle,
        squares,
):
    card_header = f'''
    <html lang="en"><head>

      <meta charset="UTF-8">

      <title>{card_title}</title>
    '''
    card_header += '''<link href="https://fonts.googleapis.com/css?family=Amatic+SC:700|Nunito|Caveat+Brush" rel="stylesheet">

      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/simple-line-icons/2.4.1/css/simple-line-icons.min.css">

    <style>
    * {
      box-sizing: border-box;
    }

    body {
      background: #f8f8f8;
      font-family: "Nunito", sans-serif;
    }

    aside.context {
      text-align: center;
      color: #333;
      line-height: 1.7;
    }
    aside.context a {
      text-decoration: none;
      color: #333;
      padding: 3px 0;
      border-bottom: 1px dashed;
    }
    aside.context a:hover {
      border-bottom: 1px solid;
    }
    aside.context .explanation {
      max-width: 700px;
      margin: 4em auto 0;
    }

    footer {
      text-align: center;
      margin: 3em auto;
      width: 100%;
    }
    footer a {
      text-decoration: none;
      display: inline-block;
      width: 45px;
      height: 45px;
      border-radius: 50%;
      background: transparent;
      border: 1px dashed #333;
      color: #333;
      margin: 5px;
    }
    footer a:hover {
      background: rgba(255, 255, 255, 0.1);
    }
    footer a .icons {
      margin-top: 12px;
      display: inline-block;
      font-size: 20px;
    }

    .main-content {
      max-width: 600px;
      width: 100%;
      margin: 4em auto 0;
      overflow: hidden;
    }

    .title {
      background: #fdb90b;
      color: #fff;
      padding: 30px 10px;
      grid-column: span 5;
      text-align: center;
      font: 72px/0.9 "Amatic SC", cursive;
    }
    .title span {
      display: none;
    }
    .title span:nth-child(1) {
      display: block;
    }
    @media screen and (max-width: 600px) {
      .title span:nth-child(1) {
        display: none;
      }
      .title span:nth-child(2) {
        display: block;
      }
    }

    .bingo-card {
      background: #f7d75c;
      padding: 10px;
      display: grid;
      grid-gap: 3px;
      grid-template-rows: repeat(5, 110px);
      grid-template-columns: repeat(5, 1fr);
      text-transform: uppercase;
    }
    .bingo-card__item {
      background: #f9f59e;
      display: flex;
      align-items: center;
      text-align: center;
      justify-content: center;
      position: relative;
      cursor: pointer;
      font-size: 12px;
      line-height: 1.35;
      user-select: none;
    }
    .bingo-card__item:after {
      content: "-";
      position: absolute;
      top: -28%;
      left: -30%;
      color: #fbda7d;
      width: 100%;
      opacity: 0;
      transition: 0.1s ease;
      height: 0;
      pointer-events: none;
      font: 280px/0.5 "Caveat Brush", cursive;
      text-align: center;
      transform: rotate(-45deg);
    }
    .bingo-card__item.active:after {
      height: 100%;
      opacity: 0.7;
    }

    .bingo-card__item {
      padding: 15px;
    }
    .bingo-card__item.active .bingo-card__checkbox:before {
      content: "\2714";
      position: absolute;
      color: black;
      left: 0;
      top: -19px;
      color: #fdb90b;
      font: 30px "Caveat Brush", cursive;
    }
    .bingo-card__checkbox {
      display: none;
    }

    .clear-button {
      margin: 2em 0 0;
      font: 700 16px 'Nunito', sans-serif;
      text-transform: uppercase;
      cursor: pointer;
      display: inline-block;
      border: 2px dotted;
      color: #fdb90b;
      padding: 8px 10px;
    }
    .clear-button:hover {
      color: #f2ae00;
    }

    @media screen and (max-width: 600px) {
      .main-content {
        max-width: none;
        margin: 0;
      }

      .title {
        font: 50px/0.9 "Amatic SC", cursive;
        padding: 20px;
      }

      .bingo-card {
        grid-template-rows: repeat(24, auto);
        grid-template-columns: auto;
        margin: 1em;
      }

      .bingo-card__item {
        justify-content: flex-start;
        padding: 15px 15px 15px 40px;
        text-align: left;
      }
      .bingo-card__item:after {
        content: "";
        opacity: 0;
      }
      .bingo-card__item:nth-child(13) {
        display: none;
      }

      .bingo-card__checkbox {
        display: inline;
        position: absolute;
        width: 20px;
        height: 20px;
        left: 10px;
        border: 2px dashed #f7d75c;
      }
    }
    </style>

      <script>
      window.console = window.console || function(t) {};
    </script>



      <script>
      if (document.location.search.match(/type=embed/gi)) {
        window.parent.postMessage("resize", "*");
      }
    </script>


    </head>
    '''

    card_content = f'''
    <body translate="no">
      <div class="main-content">
      <div class="title"> <span>{card_title}</span><br><span>{card_subtitle}</span></div>
      <div class="bingo-card">
    '''
    for square in squares:
        card_content += f'''<div class="bingo-card__item">{square}<span class="bingo-card__checkbox"></span></div>'''
    card_footer = '''
      </div>
    </div>
    <aside class="context">
      <div class="clear-button">Clear board</div>
    </aside>
    <footer><a href="https://twitter.com/meowlivia_" target="_blank"><i class="icon-social-twitter icons"></i></a><a href="https://github.com/oliviale" target="_blank"><i class="icon-social-github icons"></i></a><a href="https://dribbble.com/oliviale" target="_blank"><i class="icon-social-dribbble icons"></i></a></footer>
        <script src="https://static.codepen.io/assets/common/stopExecutionOnTimeout-157cd5b220a5c80d4ff8e0e70ac069bffd87a61252088146915e8726e5d9f147.js"></script>

      <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

          <script id="rendered-js">
    $(".bingo-card__item").on('click', function () {
      $(this).toggleClass('active');
    });

    $('.clear-button').on('click', function () {
      $('.bingo-card__item').removeClass('active');
    });
    //# sourceURL=pen.js
        </script>
    </body></html>
    '''

    return card_header + card_content + card_footer
