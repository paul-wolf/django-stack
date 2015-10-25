Sample Django Project
=====================

The scripts in this repo let you install a pretty generic Django
project with one dummy app. The purpose of this project is a quick
setup of a running Django stack with a single command (after
prerequisites are installed).

The stack:

* Django
* Nginx
* uWSGI 
* Postgresql
* Django REST Framework (DRF)

All this on a single host. It will mirror the repo inside the vm. You
can edit files and use git in your host OS. Changes will be mirrored
inside the project directory in the Ubuntu vm. The application will be
available at:

<https://localhost:7081/>

Note we use HTTPS. The DRF browsable api is at:

<https://localhost:7081/api/>

This project has a test app called 'msg' that contains a test model
that can be accessed via token authorisation with Django REST
Framework using a ModelViewSet. The setup will create a user called
'admin', password 'admin'. It will create a DRF token for this user as
well.

Other details of the installation:

* Passwords: passwords, Django secret key, certs are all totally
  insecure because they are publically known. You should change them.

* Unpinned Python modules: the `requirements.txt` file does not pin
  module versions. You should do so normally.

* Project name: The project is called `mysite`. You can change this
  editing the file `deployment/env_vars/base.yml`. Change the
  `project_name` and `application_name` variables to the name you
  want. Then edit `Vagrantfile` to change the
  `config.vm.synced_folder` variable to point to the new directory
  name in the vm.

* BASE_DIR: we install into `/var/prj/mysite` (unless you change the name as per above).

* Ubuntu: this is the user owning the project.

* Postgresql: uses md5 security for the user `db_user`. See the
  pg_hba.conf file.

* Virtualenv: Django runs in a virtualenv `venv` located in the
  BASE_DIR.

* Self-signed certs: nginx uses self-signed certificates (in
  `BASE_DIR/system/certs`). When you browse to the project page,
  you'll need to tell the browser to accept the security exception.

* Environment vars: We use the django-dotenv module to read from a
  file created during installation in the BASE_DIR called `.env`.

* `.gitignore`: we ignore `venv`, `.env` and some other files.

* Logging: logs for nginx, uwsgi and the site are in BASE_DIR/log.

* .pgpass: this file is installed in ubuntu's home directory.

* emacs: we install emacs with the ido packaage.

* `vagrant ssh`: you'll find yourself in the BASE_DIR after logging in
  because we put lines at the end of .bashrc for the vagrant and
  ubuntu users to make that happen.

> This is not intended in any way to provide a production-capable
> deployment. It is not even suitable for development outside of a
> _local_ virtual machine without modification.

Installation Overview
---------------------
Prior to using this, you must install:

* Ansible
* VirtualBox
* Vagrant

The Ansible script should provide you with the ability to load a page
at https://localhost:7081 from your host OS.

A summary of steps that are explained in more detail below:

* Install ansible
* Install Vagrant/VirtualBox
* Invoke `vagrant up`

> Make sure you change all the passwords! We provide example passwords
> that are publically viewable and therefore will not be suitable for
> any use at all whether development or production.

Install Ansible
----------------

     pip install ansible

or on Mac OS X, you might have a better experience with
homebrew. Install homebrew as per this page: <http://brew.sh/>:

     ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Then, install Ansible:

     brew install ansible

Install Vagrant/VirtualBox
---------------------------

VirtualBox: <https://www.virtualbox.org/wiki/Downloads>

Vagrant: <https://www.vagrantup.com/downloads.html> 

Install the Project
-------------------

Now, git clone this repo and go into the base directory:

     git clone git@github.com:paul-wolf/django-poc.git

Go into the deployment sub-directory:

     cd django-poc/deployment

The first time you need to load the image for ubuntu:

     vagrant box add ubuntu/trusty64

This will take some time to download the os image. Now you can try to
bring up the virtual machine.

     vagrant up

The first time this is run, it will attempt to provision the new
vm. Subsequent calls will take a much shorter time. However, after
only a short time you will be able to login:

     vagrant ssh

To just re-provision in case of changes to an ansible playbook:

    vagrant provision
	
Running Local Repo in Virtual Machine
=====================================

By default, this will mirror the main directory to /var/prj/mysite on the guest OS.

Install on a Remote Host
=====================

You really do not want to install this remotely unless you undertake
significant changes to protect the installation:

* Change all passwords (Django superuser, Postgresql user, etc.)
* Change the Django secret key
* Change the certificates
* Think of using basic auth to protect the system (nginx config)

And then don't forget to not store this information in your git
repo. The configuration we use is intended to be *simple* not
production-ready. We use a single host. A good development
environment for a professional project would probably use multiple
nodes even for the local vm deployment. Likewise, the layout of the
Django directories is not the recommended layout for a major
project.

So, if you want to still put this "out there" and you have changed passwords, etc: 

```
ansible-playbook -i hosts -l <remote_host> development.yml --skip-tags=vagrant
```

Where you need to use the correct host name. The `hosts` file must
contain the specified host and any credentials you may require.


Acknowledgements
----------------

This was based off another repo on github that I don't remember
anymore but substantially changed.

