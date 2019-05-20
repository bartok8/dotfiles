;;;
;;;
;;;

;; language
(require 'mozc)
(set-language-environment "Japanese")
(setq default-input-method "japanese-mozc")
(prefer-coding-system 'utf-8)

;; package
(require 'package)
(add-to-list 'package-archives
	     '("melpa" . "http://melpa.milkbox.net/packages/"))
(add-to-list 'package-archives
	     '("marmalade" . "http://marmalade-repo.org/packages/"))
(fset 'package-desc-vers 'package--ac-desc-version)
(package-initialize)

;; navi2ch
(setq navi2ch-net-http-proxy "localhost:8080")
(setq navi2ch-article-auto-range nil)

;;; browse-url
(setq browse-url-browser-function 'browse-url-generic
      browse-url-generic-program "vivaldi")

;; デフォルト フォント
;; (set-face-attribute 'default nil :family "Migu 1M" :height 110)
(set-face-font 'default "Migu 1M-11:antialias=standard")

;; プロポーショナル フォント
;; (set-face-attribute 'variable-pitch nil :family "Migu 1M" :height 110)
(set-face-font 'variable-pitch "Migu 1M-11:antialias=standard")

;; 等幅フォント
;; (set-face-attribute 'fixed-pitch nil :family "Migu 1M" :height 110)
(set-face-font 'fixed-pitch "Migu 1M-11:antialias=standard")

;; ツールチップ表示フォント
;; (set-face-attribute 'tooltip nil :family "Migu 1M" :height 90)
(set-face-font 'tooltip "Migu 1M-9:antialias=standard")

;;; fontset

;; フォントサイズ調整
(global-set-key (kbd "C-<wheel-up>")   '(lambda() (interactive) (text-scale-increase 1)))
(global-set-key (kbd "C-=")            '(lambda() (interactive) (text-scale-increase 1)))
(global-set-key (kbd "C-<wheel-down>") '(lambda() (interactive) (text-scale-decrease 1)))
(global-set-key (kbd "C--")            '(lambda() (interactive) (text-scale-decrease 1)))

;; フォントサイズ リセット
(global-set-key (kbd "M-0") '(lambda() (interactive) (text-scale-set 0)))

(setq default-frame-alist
;;;      (append '((width                . 85)  ; フレーム幅
;;;                (height               . 38 ) ; フレーム高
      (append '((width                . 100)  ; フレーム幅
                (height               . 50 ) ; フレーム高
             ;; (left                 . 70 ) ; 配置左位置
             ;; (top                  . 28 ) ; 配置上位置
                (line-spacing         . 0  ) ; 文字間隔
                (left-fringe          . 10 ) ; 左フリンジ幅
                (right-fringe         . 11 ) ; 右フリンジ幅
                (menu-bar-lines       . 1  ) ; メニューバー
                (tool-bar-lines       . 1  ) ; ツールバー
                (vertical-scroll-bars . 1  ) ; スクロールバー
                (scroll-bar-width     . 17 ) ; スクロールバー幅
                (cursor-type          . box) ; カーソル種別
                (alpha                . 100) ; 透明度
                ) default-frame-alist) )
(setq initial-frame-alist default-frame-alist)

;; フレーム タイトル
(setq frame-title-format
      '("emacs " emacs-version (buffer-file-name " - %f")))

;; 初期画面の非表示（有効：t、無効：nil）
(setq inhibit-startup-message nil)
(setq inhibit-startup-screen nil)

;; 行番号の表示（有効：t、無効：nil）
(line-number-mode t)

;; 列番号の表示（有効：t、無効：nil）
(column-number-mode t)

;; hline
(global-hl-line-mode t)

;; key
;;;(global-set-key "\C-h" 'delete-backward-char)
(keyboard-translate ?\C-h ?\C-?)
(global-set-key "\C-j" 'scroll-down)
(global-set-key "\C-co" 'occur)
(global-set-key "\C-cg" 'goto-line)
(global-set-key "\C-x?" 'help-for-help)
(global-set-key "\C-o" 'toggle-input-method)

;; tab
(setq-default tab-width 4)

;; theme
;;;(load-theme 'deeper-blue t)

;; recentf
(require 'recentf)
(setq recentf-max-saved-items 1000)

;; paren
(show-paren-mode 1)
(setq show-paren-delay 0)
(setq show-paren-style 'expression)
(set-face-attribute 'show-paren-match-face nil
                    :background nil :foreground nil
					:weight 'extra-bold)
;;;                    :underline "#ffff00" :weight 'extra-bold)

;;; line
(setq-default line-spacing 5)

;; nlinum
;; バッファの左側に行番号を表示する
(global-nlinum-mode t)
;; 5 桁分の表示領域を確保する
(setq nlinum-format "%5d ")

;;; ends here.
