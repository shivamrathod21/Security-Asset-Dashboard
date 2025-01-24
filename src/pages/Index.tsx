import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Shield, Server, Database, AlertCircle, Search, Filter, Download, RefreshCw } from "lucide-react";
import { AddAssetDialog } from "@/components/AddAssetDialog";
import { useToast } from "@/hooks/use-toast";
import { Input } from "@/components/ui/input";
import { useState } from "react";

const Index = () => {
  const { toast } = useToast();
  const [searchQuery, setSearchQuery] = useState("");

  const handleGenerateReport = () => {
    toast({
      title: "Generating Report",
      description: "Your report is being generated and will be ready shortly.",
    });
  };

  const handleViewAllAssets = () => {
    toast({
      title: "Loading Assets",
      description: "Fetching all assets from the system.",
    });
  };

  const handleRefresh = () => {
    toast({
      title: "Refreshing Dashboard",
      description: "Updating dashboard with latest data.",
    });
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 p-6">
      {/* Header with Search */}
      <div className="mb-8 flex flex-col md:flex-row md:items-center md:justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold text-gray-900 dark:text-white">Security Asset Dashboard</h1>
          <p className="text-gray-600 dark:text-gray-400 mt-2">Monitor and manage your security assets</p>
        </div>
        <div className="flex items-center gap-2">
          <div className="relative">
            <Search className="absolute left-2 top-2.5 h-4 w-4 text-gray-500" />
            <Input
              placeholder="Search assets..."
              className="pl-8 w-[250px]"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
          </div>
          <Button variant="outline" size="icon" onClick={handleRefresh}>
            <RefreshCw className="h-4 w-4" />
          </Button>
        </div>
      </div>

      {/* Stats Overview */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <Card className="p-6 hover:shadow-lg transition-shadow">
          <div className="flex items-center gap-4">
            <div className="p-3 bg-purple-100 dark:bg-purple-900 rounded-lg">
              <Shield className="h-6 w-6 text-purple-600 dark:text-purple-300" />
            </div>
            <div>
              <p className="text-sm font-medium text-gray-600 dark:text-gray-400">Total Assets</p>
              <p className="text-2xl font-bold text-gray-900 dark:text-white">247</p>
              <p className="text-xs text-green-600 dark:text-green-400 mt-1">↑ 12% from last month</p>
            </div>
          </div>
        </Card>

        <Card className="p-6 hover:shadow-lg transition-shadow">
          <div className="flex items-center gap-4">
            <div className="p-3 bg-blue-100 dark:bg-blue-900 rounded-lg">
              <Server className="h-6 w-6 text-blue-600 dark:text-blue-300" />
            </div>
            <div>
              <p className="text-sm font-medium text-gray-600 dark:text-gray-400">Active Devices</p>
              <p className="text-2xl font-bold text-gray-900 dark:text-white">189</p>
              <p className="text-xs text-green-600 dark:text-green-400 mt-1">↑ 8% from last month</p>
            </div>
          </div>
        </Card>

        <Card className="p-6 hover:shadow-lg transition-shadow">
          <div className="flex items-center gap-4">
            <div className="p-3 bg-green-100 dark:bg-green-900 rounded-lg">
              <Database className="h-6 w-6 text-green-600 dark:text-green-300" />
            </div>
            <div>
              <p className="text-sm font-medium text-gray-600 dark:text-gray-400">Software Licenses</p>
              <p className="text-2xl font-bold text-gray-900 dark:text-white">156</p>
              <p className="text-xs text-yellow-600 dark:text-yellow-400 mt-1">→ No change</p>
            </div>
          </div>
        </Card>

        <Card className="p-6 hover:shadow-lg transition-shadow">
          <div className="flex items-center gap-4">
            <div className="p-3 bg-red-100 dark:bg-red-900 rounded-lg">
              <AlertCircle className="h-6 w-6 text-red-600 dark:text-red-300" />
            </div>
            <div>
              <p className="text-sm font-medium text-gray-600 dark:text-gray-400">Critical Alerts</p>
              <p className="text-2xl font-bold text-gray-900 dark:text-white">12</p>
              <p className="text-xs text-red-600 dark:text-red-400 mt-1">↑ 3 new alerts</p>
            </div>
          </div>
        </Card>
      </div>

      {/* Quick Actions */}
      <div className="mb-8">
        <h2 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">Quick Actions</h2>
        <div className="flex flex-wrap gap-4">
          <AddAssetDialog />
          <Button variant="outline" onClick={handleGenerateReport} className="gap-2">
            <Download className="h-4 w-4" />
            Generate Report
          </Button>
          <Button variant="outline" onClick={handleViewAllAssets} className="gap-2">
            <Filter className="h-4 w-4" />
            View All Assets
          </Button>
        </div>
      </div>

      {/* Recent Activity Section */}
      <div>
        <h2 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">Recent Activity</h2>
        <Card className="p-6">
          <div className="space-y-4">
            {[
              { text: "New device registered: Firewall-DC1", time: "2 minutes ago", type: "addition" },
              { text: "License updated: Endpoint Protection Suite", time: "1 hour ago", type: "update" },
              { text: "Alert resolved: Server-DB2 patch status", time: "3 hours ago", type: "resolution" },
              { text: "Asset decommissioned: Legacy-Switch-01", time: "5 hours ago", type: "removal" }
            ].map((activity, index) => (
              <div key={index} className="flex items-center justify-between py-2 border-b last:border-0 dark:border-gray-700">
                <div className="flex items-center gap-4">
                  <div className={`w-2 h-2 rounded-full ${
                    activity.type === 'addition' ? 'bg-green-600' :
                    activity.type === 'update' ? 'bg-blue-600' :
                    activity.type === 'resolution' ? 'bg-yellow-600' :
                    'bg-red-600'
                  }`}></div>
                  <p className="text-gray-600 dark:text-gray-300">{activity.text}</p>
                </div>
                <span className="text-sm text-gray-500 dark:text-gray-400">{activity.time}</span>
              </div>
            ))}
          </div>
        </Card>
      </div>
    </div>
  );
};

export default Index;