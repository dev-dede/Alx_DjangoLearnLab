# Django Permissions & Groups Setup

## Overview
This project implements a role-based access control system using Django's built-in permissions and groups.

## Permissions
- `can_view`: Allows viewing articles.
- `can_create`: Allows creating new articles.
- `can_edit`: Allows editing existing articles.
- `can_delete`: Allows deleting articles.

## User Groups
- **Viewers**: Can only view articles.
- **Editors**: Can create and edit articles.
- **Admins**: Have all permissions.

## How to Set Up
1. Run migrations: `python manage.py migrate`
2. Create groups and assign permissions:
   ```sh
   python manage.py shell < setup_groups.py
