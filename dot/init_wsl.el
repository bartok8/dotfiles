;;;
;;;
;;;

;; language
;;(require 'mozc)
(set-language-environment "Japanese")
;;(setq default-input-method "japanese-mozc")
(prefer-coding-system 'utf-8)

;; package
(require 'package)
(add-to-list 'package-archives
;;;	     '("melpa" . "http://melpa.milkbox.net/packages/"))
			 '("melpa" . "http://melpa.org/packages/"))
;;;(add-to-list 'package-archives
;;;	     '("melpa-stable" . "https://stable.melpa.org/packages/"))
(add-to-list 'package-archives
	     '("marmalade" . "http://marmalade-repo.org/packages/"))
(fset 'package-desc-vers 'package--ac-desc-version)
(package-initialize)

;; navi2ch
;;;(require 'navi2ch)
(setq navi2ch-net-http-proxy "localhost:8080")
(setq navi2ch-article-auto-range nil)

;;; browse-url
(setq browse-url-browser-function 'browse-url-generic
      browse-url-generic-program "vivaldi")

;; ;; デフォルト フォント
;; ;; (set-face-attribute 'default nil :family "Migu 1M" :height 110)
;; (set-face-font 'default "Migu 1M-11:antialias=standard")

;; ;; プロポーショナル フォント
;; ;; (set-face-attribute 'variable-pitch nil :family "Migu 1M" :height 110)
;; (set-face-font 'variable-pitch "Migu 1M-11:antialias=standard")

;; ;; 等幅フォント
;; ;; (set-face-attribute 'fixed-pitch nil :family "Migu 1M" :height 110)
;; (set-face-font 'fixed-pitch "Migu 1M-11:antialias=standard")

;; ;; ツールチップ表示フォント
;; ;; (set-face-attribute 'tooltip nil :family "Migu 1M" :height 90)
;; (set-face-font 'tooltip "Migu 1M-9:antialias=standard")

;; ;;; fontset

;; ;; フォントサイズ調整
;; (global-set-key (kbd "C-<wheel-up>")   '(lambda() (interactive) (text-scale-increase 1)))
;; (global-set-key (kbd "C-=")            '(lambda() (interactive) (text-scale-increase 1)))
;; (global-set-key (kbd "C-<wheel-down>") '(lambda() (interactive) (text-scale-decrease 1)))
;; (global-set-key (kbd "C--")            '(lambda() (interactive) (text-scale-decrease 1)))

;; ;; フォントサイズ リセット
;; (global-set-key (kbd "M-0") '(lambda() (interactive) (text-scale-set 0)))

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

(set-face-attribute 'default nil :height 170)

(setq default-frame-alist
      (append '((width                . 110)  ; フレーム幅
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
(setq window-system-default-frame-alist default-frame-alist)

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
(load-theme 'deeper-blue t)

;; recentf
(require 'recentf)
(setq recentf-max-saved-items 1000)

;; paren
(show-paren-mode 1)
(setq show-paren-delay 0)
(setq show-paren-style 'expression)
;;;(set-face-attribute 'show-paren-match-face nil
;;;                    :background nil :foreground nil
;;;					:weight 'extra-bold)

;;;                    :underline "#ffff00" :weight 'extra-bold)

;;; line
(setq-default line-spacing 5)

;; nlinum
;; バッファの左側に行番号を表示する
;;;(global-nlinum-mode t)
;;;(global-linum-mode t)
;; 5 桁分の表示領域を確保する
;;;(setq nlinum-format "%5d ")

;; 設定ファイルで有効化
(global-display-line-numbers-mode 1)  // グローバル
(add-hook 'prog-mode-hook 'display-line-numbers-mode)  // プログラミングモードのみ
;; 絶対行番号（デフォルト）
(setq display-line-numbers-type t)
;; 相対行番号
(setq display-line-numbers-type 'relative)
;; 視覚的な行番号（折り畳みやラップを考慮）
(setq display-line-numbers-type 'visual)

;;; ends here.
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages (quote (navi2ch wanderlust))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
