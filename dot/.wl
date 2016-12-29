;;; -*- Emacs-Lisp -*-
;;;
;;;

(setq mime-edit-split-message nil)

;; IMAP, gmail:
(setq elmo-imap4-default-server "imap.gmail.com"
      elmo-imap4-default-user "bartok8@gmail.com"
      elmo-imap4-default-authenticate-type 'clear
      elmo-imap4-default-port '993
      elmo-imap4-default-stream-type 'ssl

      ;;for non ascii-characters in folder-names
      elmo-imap4-use-modified-utf7 t)

;; SMTP
(setq wl-smtp-connection-type 'starttls
      wl-smtp-posting-port 587
      wl-smtp-authenticate-type "plain"
      wl-smtp-posting-user "bartok8"
      wl-smtp-posting-server "smtp.gmail.com"
      wl-local-domain "gmail.com"
      wl-message-id-domain "smtp.gmail.com")

(setq wl-from "NOGUCHI Satoru <bartok8@gmail.com>"
	  ;;all system folders (draft, trash, spam, etc) are placed in the
	  ;;[Gmail]-folder, except inbox. "%" means it's an IMAP-folder
	  wl-default-folder "%inbox"
	  wl-draft-folder   "%[Gmail]/Drafts"
	  wl-trash-folder   "%[Gmail]/Trash"
	  wl-fcc            "%[Gmail]/Sent"

	  ;; mark sent messages as read (sent messages get sent back to you and
	  ;; placed in the folder specified by wl-fcc)
	  wl-fcc-force-as-read    t

	  ;;for when auto-compleating foldernames
	  wl-default-spec "%")

(defun wl-summary-overview-entity-compare-by-reply-date (a b)
  "Compare entity A and B by latest date of replies."
  (let ((fx
		 #'(lambda (x)
			 (let* ((number (elmo-message-entity-number x))
					(list (cons number
								(wl-thread-entity-get-descendant
								 (wl-thread-get-entity number))))
					max time)
			   (while list
				 (when (condition-case nil
						   (elmo-time-less-p
							max
							(setq time
								  (elmo-message-entity-field
								   (elmo-message-entity
									wl-summary-buffer-elmo-folder (car list))
								   'date)))
						 (error nil))
				   (setq max time))
				 (setq list (cdr list)))
			   max))))
	(condition-case nil
		(elmo-time-less-p (funcall fx a) (funcall fx b))
	  (error nil))))
(add-to-list 'wl-summary-sort-specs 'reply-date)

(defun wl-summary-overview-entity-compare-by-reply-number (a b)
  "Compare entity A and B by latest number of replies."
  (let ((fx #'(lambda (x)
				(setq x (elmo-message-entity-number x))
				(apply 'max x (wl-thread-entity-get-descendant 
							   (wl-thread-get-entity x))))))
	(< (funcall fx a) (funcall fx b))))
(add-to-list 'wl-summary-sort-specs 'reply-number)

;;; ends here.
