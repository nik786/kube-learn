import argparse

# -------- DASHBOARDS --------
from dashboards.dashboard_backup import (
    backup_dashboards,
    restore_dashboards_from_s3,
    restore_dashboards_to_grafana
)

# -------- ALERTS --------
from alerts.alerts_backup import (
    backup_alerts,
    restore_alerts_from_s3,
    restore_alerts_to_grafana
)

# -------- CONTACT POINTS --------
from contact_points.contact_points_backup import (
    backup_contact_points,
    restore_contact_points_from_s3,
    restore_contact_points_to_grafana
)

# -------- DATASOURCES --------
from datasources.datasource_backup import (
    backup_datasources
)

# -------- DATA --------
from data.get_data import (
    get_data
)


# =========================================================
# HELPER
# =========================================================
def parse_comma_list(value):

    if not value:
        return None

    value = value.strip()

    # Handle ALL
    if value.lower() == "all":
        return None

    return [
        v.strip()
        for v in value.split(",")
        if v.strip()
    ]


# =========================================================
# MAIN
# =========================================================
def main():

    parser = argparse.ArgumentParser(
        description="Grafana Backup & Restore Tool"
    )

    # =====================================================
    # COMMON
    # =====================================================
    parser.add_argument(
        "--action",
        required=True
    )

    parser.add_argument(
        "--env",
        choices=["syst", "test", "prod"],
        default="syst"
    )

    # =====================================================
    # DASHBOARDS
    # =====================================================
    parser.add_argument(
        "--upload_dashboard_ids",
        help="Use 'all' or comma separated dashboard UIDs"
    )

    # =====================================================
    # ALERTS
    # =====================================================
    parser.add_argument(
        "--upload_alert_names",
        help="Use 'all' or comma separated alert names"
    )

    # =====================================================
    # CONTACT POINTS
    # =====================================================
    parser.add_argument(
        "--upload_contact_point_names",
        help="Use 'all' or comma separated contact point names"
    )

    # =====================================================
    # DATASOURCES
    # =====================================================
    parser.add_argument(
        "--upload_datasource_ids",
        help="Use 'all' or comma separated datasource UIDs"
    )

    # =====================================================
    # RESTORE
    # =====================================================
    parser.add_argument(
        "--date",
        help="Backup date folder"
    )

    parser.add_argument(
        "--files",
        help="Comma separated backup file names"
    )

    args = parser.parse_args()

    files = parse_comma_list(args.files)

    # =====================================================
    # DASHBOARDS
    # =====================================================
    if args.action == "backup_dashboards":

        dashboard_ids = parse_comma_list(
            args.upload_dashboard_ids
        )

        backup_dashboards(
            env=args.env,
            names=dashboard_ids
        )

    elif args.action == "restore_dashboards_from_s3":

        if not args.date:
            print("❌ --date is required")
            return

        restore_dashboards_from_s3(
            env=args.env,
            date=args.date,
            files=files,
            db_type="syst"
        )

    elif args.action == "restore_dashboards_to_grafana":

        if not args.date:
            print("❌ --date is required")
            return

        restore_dashboards_to_grafana(
            env=args.env,
            date=args.date,
            files=files,
            db_type="syst"
        )

    # =====================================================
    # DATASOURCES
    # =====================================================
    elif args.action == "backup_datasources":

        datasource_ids = parse_comma_list(
            args.upload_datasource_ids
        )

        backup_datasources(
            args.env,
            datasource_ids
        )

    # =====================================================
    # ALERTS
    # =====================================================
    elif args.action == "backup_alerts":

        alert_names = parse_comma_list(
            args.upload_alert_names
        )

        backup_alerts(
            args.env,
            alert_names
        )

    elif args.action == "restore_alerts_from_s3":

        if not args.date:
            print("❌ --date is required")
            return

        restore_alerts_from_s3(
            args.env,
            args.date,
            files,
            "syst"
        )

    elif args.action == "restore_alerts_to_grafana":

        if not args.date:
            print("❌ --date is required")
            return

        restore_alerts_to_grafana(
            args.env,
            args.date,
            files,
            "syst"
        )

    # =====================================================
    # CONTACT POINTS
    # =====================================================
    elif args.action == "backup_contact_points":

        contact_point_names = parse_comma_list(
            args.upload_contact_point_names
        )

        backup_contact_points(
            args.env,
            contact_point_names
        )

    elif args.action == "restore_contact_points_from_s3":

        if not args.date:
            print("❌ --date is required")
            return

        restore_contact_points_from_s3(
            args.env,
            args.date,
            files
        )

    elif args.action == "restore_contact_points_to_grafana":

        if not args.date:
            print("❌ --date is required")
            return

        restore_contact_points_to_grafana(
            args.env,
            args.date,
            files
        )

    # =====================================================
    # GET DATA
    # =====================================================
    elif args.action == "get_data":

        get_data(args.env)

    # =====================================================
    # INVALID ACTION
    # =====================================================
    else:

        print("❌ Invalid action")


# =========================================================
# ENTRYPOINT
# =========================================================
if __name__ == "__main__":
    main()

