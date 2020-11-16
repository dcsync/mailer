Mailer
======

Mailer is a multi-threaded mass-mailing script for phishing.

It accepts email templates in .eml format and supports `%To_Name%` template
tokens (similar to Cobalt Strike).

The target list may contain email addresses in `Name <name@example.com>` or
`name@example.com<tab>Name` formats.

Here's an example:

    $ cat Phish.eml
    MIME-Version: 1.0
    Content-Type: multipart/alternative;
     boundary="=e380ffc1cee42e2090eb25464a93b84b"
    Date: Mon, 01 Apr 2019 07:16:11 -0100
    From: real.person@company.com
    To: real.person@company.com
    Subject: Urgent: Open this Document
    --=e380ffc1cee42e2090eb25464a93b84b
    Content-Transfer-Encoding: 7bit
    Content-Type: text/plain; charset=US-ASCII
    
    Hi %To_Name%,
    
    Please open this document immediately: https://company.com/files/1435994.
    
    Thanks!
    --=e380ffc1cee42e2090eb25464a93b84b--
    
    $ cat targets.list
    john.smith@target.com	John Smith
    Dave <dave@target.com>
    admin@target.com	Mark
    
    $ ./Mailer --template Phish.eml --target-file targets.list --server phishing_server --user real.person@company.com --password password123 --from-name 'Real Person'
    [+] Mailing to 3 target(s)
    [+] Success: Dave <dave@target.com>
    [+] Success: Mark <admin@target.com>
    [+] Success: John Smith <john.smith@target.com>

For more options:

    $ ./Mailer -h
    usage: Mailer [-h] -f TARGET_FILE [--no-shuffle] [--timeout TIMEOUT]
                  [-T MAX_THREADS] -s SERVER [-P PORT] [--no-tls] -u USER -p
                  PASSWORD [-d DELAY] -t TEMPLATE [--from-email FROM_EMAIL]
                  [--from-name FROM_NAME] [--subject SUBJECT] [--cc CC]
                  [--no-encoding] [--no-generated-plaintext] [--no-replace-tokens]
                  [--no-random-message-id] [--no-clean-headers] [-D]
    
    optional arguments:
      -h, --help            show this help message and exit
      -f TARGET_FILE, --target-file TARGET_FILE
                            file containing email addresses to mail to (in
                            email@example.com, 'First Last <email@example.com>',
                            or 'email@example.com\tFirst Last' formats)
      --no-shuffle          do not shuffle target list
      --timeout TIMEOUT     SMTP timeout (default: 30)
      -T MAX_THREADS, --max-threads MAX_THREADS
                            maximum number of mailing threads (default: 10)
      -s SERVER, --server SERVER
                            server to submit to
      -P PORT, --port PORT  server to submit to (default: 465)
      --no-tls              do not use TLS
      -u USER, --user USER  login user
      -p PASSWORD, --password PASSWORD
                            login password
      -d DELAY, --delay DELAY
                            random delay up to X seconds
      -t TEMPLATE, --template TEMPLATE
                            .eml template
      --from-email FROM_EMAIL
                            from email (default: value of --user)
      --from-name FROM_NAME
                            from name (default: value of --from-email)
      --subject SUBJECT     email subject
      --cc CC               CC line
      --no-encoding         do not base64 encode email parts
      --no-generated-plaintext
                            do not generate plaintext if message is HTML
      --no-replace-tokens   do not replace %To_Name% tokens in text or subject
      --no-random-message-id
                            do not add a random Message-ID header
      --no-clean-headers    do not remove X- and Delivered-To headers
      -D, --debug           debug mode
