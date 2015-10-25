(add-to-list 'load-path "~/.emacs.d/lisp")

(require 'ido)
    (ido-mode t)

(require 'recentf)
    (recentf-mode 1)
    (setq recentf-max-menu-items 25)
    (global-set-key "\C-x\ \C-r" 'recentf-open-files)

;; .emacs
;;(add-to-list 'load-path "~/.emacs.d/lisp/")

;;; uncomment this line to disable loading of "default.el" at startup
;; (setq inhibit-default-init t)

;; enable visual feedback on selections
;(setq transient-mark-mode t)

;; default to better frame titles
;;(setq frame-title-format
;;      (concat  "%b - emacs@" (system-name)))

;; default to unified diffs
(setq diff-switches "-u")
