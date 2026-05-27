import argparse
import os

# =========================================================
# DASHBOARDS
# =========================================================
from dashboards.dashboard_backup import (
    backup_dashboards,
    restore_dashboards_from_s3,
    restore_dashboards_to_grafana
)

# =========================================================
# ALERTS
# =========================================================
from alerts.alerts_backup import (
    backup_alerts,
    restore_alerts_from_s3,
    restore_alerts_to_grafana
)

# =========================================================
# CONTACT POINTS
# =========================================================
from contact_points.contact_points_backup import (
    backup_contact_points,
    restore_contact_points_from_s3,
    restore_contact_points_to_grafana
)

# =========================================================
# DATASOURCES
# =========================================================
from datasources.datasource_backup import (
    backup_datasources
)

# =========================================================
# DATA
# =========================================================
from data.get_data import (
    get_data
)


# =========================================================
# HELPER
# =========================================================
def parse_input(cli_value=None, env_var=None):

    """
    Priority:
    CLI arg > ENV var > empty
    """

    value = cli_value or os.getenv(env_var)

    # Skip module if empty
    if not value:
        return []

    value = value.strip()

    # Handle ALL
    if value.lower() == "all":
        return "all"

    # Handle comma separated list
    return [
        item.strip()
        for item in value.split(",")
        if item.strip()
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

    # =====================================================
    # COMMON PARSING
    # =====================================================
    files = parse_input(args.files)

    # =====================================================
    # BACKUP ALL
    # =====================================================
    if args.action == "backup_all":

        dashboard_ids = parse_input(
            cli_value=args.upload_dashboard_ids,
            env_var="DASHBOARD_IDS"
        )

        alert_names = parse_input(
            cli_value=args.upload_alert_names,
            env_var="ALERT_NAMES"
        )

        datasource_ids = parse_input(
            cli_value=args.upload_datasource_ids,
            env_var="DATASOURCE_IDS"
        )

        contact_point_names = parse_input(
            cli_value=args.upload_contact_point_names,
            env_var="CONTACT_POINT_NAMES"
        )

        print("\n===================================")
        print("STARTING GRAFANA BACKUP")
        print("===================================\n")

        # =================================================
        # DASHBOARDS
        # =================================================
        if dashboard_ids != []:

            try:
                print("===== BACKUP DASHBOARDS =====")

                backup_dashboards(
                    env=args.env,
                    names=dashboard_ids
                )

                print("✅ Dashboard backup completed\n")

            except Exception as e:
                print(f"❌ Dashboard backup failed: {e}\n")

        # =================================================
        # ALERTS
        # =================================================
        if alert_names != []:

            try:
                print("===== BACKUP ALERTS =====")

                backup_alerts(
                    args.env,
                    alert_names
                )

                print("✅ Alert backup completed\n")

            except Exception as e:
                print(f"❌ Alert backup failed: {e}\n")

        # =================================================
        # DATASOURCES
        # =================================================
        if datasource_ids != []:

            try:
                print("===== BACKUP DATASOURCES =====")

                backup_datasources(
                    args.env,
                    datasource_ids
                )

                print("✅ Datasource backup completed\n")

            except Exception as e:
                print(f"❌ Datasource backup failed: {e}\n")

        # =================================================
        # CONTACT POINTS
        # =================================================
        if contact_point_names != []:

            try:
                print("===== BACKUP CONTACT POINTS =====")

                backup_contact_points(
                    args.env,
                    contact_point_names
                )

                print("✅ Contact point backup completed\n")

            except Exception as e:
                print(f"❌ Contact point backup failed: {e}\n")

        print("===================================")
        print("ALL BACKUPS COMPLETED")
        print("===================================\n")

    # =====================================================
    # DASHBOARDS
    # =====================================================
    elif args.action == "backup_dashboards":

        dashboard_ids = parse_input(
            cli_value=args.upload_dashboard_ids,
            env_var="DASHBOARD_IDS"
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

        datasource_ids = parse_input(
            cli_value=args.upload_datasource_ids,
            env_var="DATASOURCE_IDS"
        )

        backup_datasources(
            args.env,
            datasource_ids
        )

    # =====================================================
    # ALERTS
    # =====================================================
    elif args.action == "backup_alerts":

        alert_names = parse_input(
            cli_value=args.upload_alert_names,
            env_var="ALERT_NAMES"
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

        contact_point_names = parse_input(
            cli_value=args.upload_contact_point_names,
            env_var="CONTACT_POINT_NAMES"
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

